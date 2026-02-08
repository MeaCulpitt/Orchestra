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
│    │◀── Contribution ──────│                      │              │
│    │   reward              │                      │              │
│    │                       │   [If rejected]      │              │
│    │◀── Stake slashed ─────│                      │              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Verification by Proposal Type

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
            reward(prop.miner, FULL_REWARD)
            
            # Later valid proposals get confirmation bonus
            for later in sorted_props[1:]:
                if verify(later):
                    reward(later.miner, CONFIRMATION_REWARD)
            return
    
    # No valid proposals
    for prop in sorted_props:
        slash(prop.miner)
```

---

## Scoring Formulas

### Orchestration Score (60% of total)

```
S_orch = (0.20 × hash_verified) + 
         (0.15 × schema_valid) + 
         (0.10 × completeness) + 
         (0.10 × routing_score) + 
         (0.05 × latency_ok)
```

### Ledger Score (40% of total)

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
    return
