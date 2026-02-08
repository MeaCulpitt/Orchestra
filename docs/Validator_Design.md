# Orchestra: Validator Architecture & Audit Logic

Orchestra validators have two responsibilities:

1. **Orchestration Auditing** — Verify miners actually called subnets and delivered quality results
2. **Ledger Governance** — Verify proposed updates against live subnets, approve or reject

Both rely on objective, verifiable criteria.

---

## Orchestration Auditing

### What Validators Check

| Check | Method | Pass/Fail |
|-------|--------|-----------|
| Hash proofs | Query subnet for transaction | Binary |
| Schema compliance | Pydantic validation | Binary |
| Completeness | Field presence check | Ratio |
| Routing quality | Compare to reference | Scored |
| Latency | Timestamp comparison | Binary |

### Worked Example

**Challenge issued:**

```json
{
  "challenge_id": "0x5c3b...",
  "objective": "Find recent AI funding rounds and summarize trends",
  "target_schema": {
    "rounds": [{"company": "str", "amount": "str", "date": "str"}],
    "trends": [{"trend": "str", "evidence": "str"}]
  }
}
```

**Miner response received:**

```json
{
  "task_pipeline": [
    {"subnet": "SN22", "hash": "0x7a3f...", "latency_ms": 310},
    {"subnet": "SN13", "hash": "0x8b4e...", "latency_ms": 920}
  ],
  "standardized_data": {
    "rounds": [
      {"company": "Lambda Labs", "amount": "$320M", "date": "2026-01-15"},
      {"company": "Together AI", "amount": "$450M", "date": "2026-01-22"}
    ],
    "trends": [
      {"trend": "GPU providers dominating", "evidence": "3 of 5 top rounds"}
    ]
  }
}
```

**Audit process:**

```python
async def audit_orchestration(response, challenge):
    scores = {}
    
    # 1. Hash verification (20%)
    hash_valid = await verify_all_hashes(response.task_pipeline)
    scores["hash"] = 1.0 if hash_valid else 0.0
    
    # 2. Schema compliance (15%)
    try:
        validate_against_schema(response.standardized_data, challenge.target_schema)
        scores["schema"] = 1.0
    except ValidationError as e:
        scores["schema"] = 1.0 - (len(e.errors()) / total_fields)
    
    # 3. Completeness (10%)
    required = get_required_fields(challenge.target_schema)
    present = count_present_fields(response.standardized_data, required)
    scores["completeness"] = present / len(required)
    
    # 4. Routing efficiency (10%)
    scores["routing"] = assess_routing(response.task_pipeline, challenge.objective)
    
    # 5. Latency (5%)
    scores["latency"] = 1.0 if response.total_latency_ms < challenge.deadline_ms else 0.0
    
    return calculate_weighted_score(scores)
```

**Result:**

| Component | Weight | Score |
|-----------|--------|-------|
| Hash verification | 20% | 1.0 |
| Schema compliance | 15% | 1.0 |
| Completeness | 10% | 1.0 |
| Routing efficiency | 10% | 0.9 |
| Latency | 5% | 1.0 |
| **Orchestration total** | 60% | **0.59** |

---

## Ledger Governance

Validators verify miner proposals against live subnet state.

### Verification Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                  LEDGER UPDATE FLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  MINER                 VALIDATORS              LEDGER            │
│    │                       │                      │              │
│    │── Propose update ────▶│                      │              │
│    │   (with evidence)     │                      │              │
│    │                       │                      │              │
│    │                       │── Test live subnet ─▶│              │
│    │                       │◀── Confirm/deny ─────│              │
│    │                       │                      │              │
│    │                       │   [If verified]      │              │
│    │                       │── Commit update ────▶│ ✓            │
│    │                       │                      │              │
│    │                       │   [If rejected]      │              │
│    │◀── Stake slashed ─────│                      │              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Verification by Proposal Type

**Schema update:**
```python
async def verify_schema_update(proposal):
    # Get current Ledger entry
    current = ledger.get(proposal.subnet_id)
    
    # Probe live subnet
    response = await probe_subnet(proposal.subnet_id)
    actual_schema = extract_schema(response)
    
    # Verify the change exists
    for change in proposal.changes:
        old_value = get_path(current, change.path)
        new_value = get_path(actual_schema, change.path)
        
        if old_value != change.old or new_value != change.new:
            return False
    
    return True
```

**New subnet discovery:**
```python
async def verify_new_subnet(proposal):
    # Probe the subnet directly
    response = await probe_subnet(proposal.subnet_id)
    
    if response is None:
        return False  # Subnet doesn't exist/respond
    
    # Compare proposed schema to actual
    actual_schema = extract_schema(response)
    proposed_schema = proposal.entry.output_schema
    
    return schemas_match(actual_schema, proposed_schema)
```

**Deprecation:**
```python
async def verify_deprecation(proposal):
    # Attempt multiple probes
    successes = 0
    for _ in range(10):
        try:
            await probe_subnet(proposal.subnet_id, timeout=5000)
            successes += 1
        except:
            pass
    
    # Confirm subnet is actually unreliable
    return successes < 3  # Less than 30% success = deprecated
```

### Conflict Resolution

Multiple miners may propose the same update:

```python
def resolve_ledger_conflict(proposals):
    # Sort by timestamp (first proposer priority)
    sorted_props = sorted(proposals, key=lambda p: p.timestamp)
    
    for prop in sorted_props:
        if verify(prop):
            # First valid proposal wins
            commit(prop)
            credit(prop.miner, FULL_WEIGHT)
            
            # Later valid proposals get confirmation bonus
            for later in sorted_props[1:]:
                if verify(later):
                    credit(later.miner, CONFIRMATION_WEIGHT)
            return
    
    # No valid proposals
    for prop in sorted_props:
        slash(prop.miner)
```

---

## Scoring

### Orchestration Score (60%)

```
S_orch = (0.20 × hash_verified) + 
         (0.15 × schema_valid) + 
         (0.10 × completeness) + 
         (0.10 × routing_score) + 
         (0.05 × latency_ok)
```

### Ledger Score (40%)

```
S_ledger = (0.20 × update_accuracy) + 
           (0.10 × discovery_bonus) + 
           (0.05 × freshness_score) + 
           (0.05 × coverage_score)
```

### Combined

```
S_total = S_orch + S_ledger
```

---

## Challenge Generation

### Synthetic Challenges

Pre-designed objectives for consistent benchmarking:

```python
SYNTHETIC_TEMPLATES = [
    {
        "type": "market_research",
        "template": "Research {topic} and identify key players",
        "reference_subnets": ["SN22", "SN13"],
        "difficulty": "medium"
    },
    {
        "type": "competitive_analysis",
        "template": "Analyze competitors in {industry} and recommend positioning",
        "reference_subnets": ["SN22", "SN13", "SN1"],
        "difficulty": "hard"
    }
]

def generate_synthetic():
    template = random.choice(SYNTHETIC_TEMPLATES)
    topic = random.choice(TOPICS[template["type"]])
    return Challenge(
        objective=template["template"].format(topic=topic),
        reference=template["reference_subnets"]
    )
```

### Organic Challenges

Real user requests routed through the network:

```python
async def handle_user_request(request):
    challenge = Challenge(
        objective=request.objective,
        target_schema=request.schema,
        is_organic=True
    )
    
    responses = await broadcast_to_miners(challenge)
    scored = [(r, score(r)) for r in responses]
    best = max(scored, key=lambda x: x[1])
    
    await deliver_to_user(request.user_id, best[0])
    return scored
```

---

## Anti-Gaming Detection

### Fabricated Hashes

**Signal:** Hash doesn't exist on subnet chain
**Action:** Zero score, blacklist consideration

### Pre-Computed Responses

**Signal:** Hash timestamp before challenge issued
**Action:** Zero score

### Stale Ledger Proposals

**Signal:** Proposal describes change that doesn't exist
**Action:** Reject + slash stake

### Copied Proposals

**Signal:** Near-identical proposals from multiple miners within short window
**Action:** Only first proposer rewarded

---

## Validator Infrastructure

### Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 8-core | 16-core |
| RAM | 32GB | 64GB |
| Storage | 200GB SSD | 500GB SSD |
| Network | 500Mbps | 1Gbps |

Higher than miners because validators must:
- Verify hashes across multiple subnets
- Run Pydantic validation on all responses
- Probe subnets for Ledger verification
- Store challenge/response history

### Software

- Bittensor validator SDK
- Pydantic
- PostgreSQL (challenge history)
- Redis (caching)
- Async HTTP client

---

## Consensus

Validators converge because most checks are deterministic:

| Check | Deterministic? |
|-------|----------------|
| Hash verification | Yes |
| Schema validation | Yes |
| Completeness | Yes |
| Routing efficiency | Mostly (reference decompositions) |
| Ledger verification | Yes (probe results) |

Validators who deviate significantly from consensus see V-Trust decay:

```python
def update_v_trust(validator):
    consensus = stake_weighted_median(all_scores)
    deviation = mean_absolute_error(validator.scores, consensus)
    
    if deviation < 0.05:
        validator.v_trust += 0.01
    elif deviation > 0.15:
        validator.v_trust -= 0.05
```

Low V-Trust = lower dividend share.

---

## Cadence

| Event | Frequency |
|-------|-----------|
| Orchestration challenges | Every 20 blocks (~4 min) |
| Ledger proposal window | Rolling (any time) |
| Ledger verification | Within 5 blocks of proposal |
| Weight commitment | Every 360 blocks (~1 hr) |
| Ledger snapshot (on-chain) | Every 100 blocks (~20 min) |

---
