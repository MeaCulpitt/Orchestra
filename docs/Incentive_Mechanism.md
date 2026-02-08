# Orchestra: Incentive & Mechanism Design

Orchestra rewards **Proof of Management** — the ability to decompose complex objectives, route to optimal subnets, and deliver structured results. The mechanism balances coordination quality (70%) with Ledger accuracy (30%), using objective metrics wherever possible.

---

## Worked Example: Scoring a Miner Response

### Challenge Issued

Validator sends objective:

```json
{
  "objective": "Find the top 5 trending AI papers this week and summarize their key contributions",
  "target_schema": {
    "papers": [{"title": "str", "authors": "list", "summary": "str", "impact": "str"}],
    "meta": {"search_date": "str", "sources": "list"}
  }
}
```

### Miner Response

```json
{
  "task_pipeline": [
    {"subnet": "SN22", "task": "search", "hash": "0x7a3f...", "verified": true},
    {"subnet": "SN13", "task": "scrape", "hash": "0x8b2c...", "verified": true},
    {"subnet": "SN1", "task": "summarize", "hash": "0x9d1e...", "verified": true}
  ],
  "standardized_data": {
    "papers": [
      {"title": "Scaling Laws for...", "authors": ["..."], "summary": "...", "impact": "..."},
      // ... 4 more papers
    ],
    "meta": {"search_date": "2026-02-08", "sources": ["arxiv", "semantic_scholar"]}
  },
  "final_synthesis": "This week's trending papers focus on..."
}
```

### Scoring Breakdown

| Component | Weight | Score | Calculation |
|-----------|--------|-------|-------------|
| **Hash verification** | 25% | 1.0 | All 3 subnet calls verified on-chain |
| **Schema compliance** | 20% | 1.0 | Output passes Pydantic validation |
| **Completeness** | 15% | 1.0 | All required fields present, 5 papers returned |
| **Routing efficiency** | 10% | 0.9 | Optimal subnet selection (minor deduction: could skip SN13) |
| **Ledger accuracy** | 30% | 0.95 | SN22 schema current, SN13 schema 2 days stale |

**Final Score:** (0.25 × 1.0) + (0.20 × 1.0) + (0.15 × 1.0) + (0.10 × 0.9) + (0.30 × 0.95) = **0.935**

---

## Emission Split: 70/30

### Coordination Pool (70% of emissions)

Rewards the miner's ability to act as a **Lead Architect**:

| Criterion | Weight | Measurement |
|-----------|--------|-------------|
| Hash verification | 25% | Binary: all subnet calls have valid on-chain proofs |
| Schema compliance | 20% | Binary: output passes target_schema validation |
| Completeness | 15% | Ratio: required fields present / total required |
| Routing efficiency | 10% | Validator assessment: were chosen subnets optimal? |

**Why mostly binary metrics:** Subjective "quality" scoring is gameable. Hash verification, schema validation, and completeness are objective. Only routing efficiency requires judgment, and it's weighted low (10%).

### Ledger Pool (30% of emissions)

Rewards maintenance of the **Subnet Ledger**:

| Criterion | Weight | Measurement |
|-----------|--------|-------------|
| Schema freshness | 15% | Age of last schema update vs. subnet's actual state |
| Coverage | 10% | Number of subnets accurately catalogued |
| Trap performance | 5% | Success rate on validator schema traps |

---

## Scoring Formula

```
S = (0.70 × S_coordination) + (0.30 × S_ledger)

Where:
  S_coordination = (0.25 × hash_verified) + (0.20 × schema_valid) + 
                   (0.15 × completeness) + (0.10 × routing_score)
  
  S_ledger = (0.15 × freshness) + (0.10 × coverage) + (0.05 × trap_score)
```

### Hash Verification (25%)

Every subnet call must have a cryptographic proof:

```python
def verify_hash(call):
    # Check that the hash corresponds to a real transaction
    # on the target subnet's blockchain
    tx = fetch_transaction(call.subnet, call.hash)
    if tx is None:
        return 0.0  # No proof = no credit
    if tx.timestamp > challenge.issued_at + TIMEOUT:
        return 0.0  # Call happened after challenge = gaming
    return 1.0
```

**Binary:** Either all calls verify (1.0) or they don't (0.0). No partial credit for faked calls.

### Schema Compliance (20%)

Output must match the target schema exactly:

```python
def validate_schema(output, target_schema):
    try:
        PydanticModel(**output)
        return 1.0
    except ValidationError as e:
        # Partial credit for minor issues
        error_ratio = len(e.errors()) / total_fields
        return max(0, 1.0 - error_ratio)
```

### Completeness (15%)

Did the miner actually complete the task?

```python
def score_completeness(output, target_schema):
    required_fields = get_required_fields(target_schema)
    present_fields = count_present(output, required_fields)
    return present_fields / len(required_fields)
```

### Routing Efficiency (10%)

Was the subnet selection optimal? This is the one subjective component:

| Scenario | Score |
|----------|-------|
| Optimal routing (best subnets for task) | 1.0 |
| Acceptable routing (works but suboptimal) | 0.7 - 0.9 |
| Wasteful routing (unnecessary calls) | 0.3 - 0.6 |
| Failed routing (wrong subnets entirely) | 0.0 |

Validators maintain reference decompositions for common task types. Novel tasks are scored more leniently.

### Ledger Freshness (15%)

How current is the miner's Subnet Ledger?

```python
def score_freshness(miner_ledger, live_state):
    stale_entries = 0
    for subnet in miner_ledger:
        if miner_ledger[subnet].schema != live_state[subnet].schema:
            stale_entries += 1
    return 1.0 - (stale_entries / len(miner_ledger))
```

### Coverage (10%)

How many subnets does the miner accurately track?

```python
def score_coverage(miner_ledger, active_subnets):
    covered = len([s for s in active_subnets if s in miner_ledger])
    return covered / len(active_subnets)
```

### Trap Performance (5%)

Validators periodically issue challenges using subnets with known schema changes:

```python
def schema_trap(miner):
    # Use a subnet that changed its schema yesterday
    trap_subnet = get_recently_changed_subnet()
    challenge = generate_challenge_requiring(trap_subnet)
    response = miner.respond(challenge)
    
    if response.ledger[trap_subnet].schema == old_schema:
        return 0.0  # Stale ledger
    return 1.0  # Current ledger
```

---

## Miner Economics

### Revenue Sources

| Source | Amount | Frequency |
|--------|--------|-----------|
| Emissions | ~0.015 TAO/challenge | Per successful challenge |
| Margin share | ~0.002 TAO/challenge | Per organic (paid) request |

### Cost Structure

| Cost | Amount | Notes |
|------|--------|-------|
| Subnet calls | 0.002-0.005 TAO/call | Varies by subnet |
| Compute | Minimal | Orchestration, not inference |
| Ledger maintenance | Time | Polling metagraph |

### Profitability Example

**Scenario:** Miner handles 100 challenges/day, 70% success rate

| Line item | Calculation | Daily |
|-----------|-------------|-------|
| Emissions earned | 70 × 0.015 TAO | 1.05 TAO |
| Margin share | 70 × 0.002 TAO | 0.14 TAO |
| Subnet costs | 70 × 0.008 TAO | (0.56 TAO) |
| Failed costs | 30 × 0.006 TAO | (0.18 TAO) |
| **Net profit** | | **0.45 TAO/day** |

**Break-even:** ~55% success rate (depends on subnet costs and emission rates)

---

## Anti-Gaming Mechanisms

### Hash Auditing

**Attack:** Miner claims to call subnets but fabricates responses.

**Defense:** Every call requires a verifiable on-chain transaction hash. Validators cross-reference hashes against subnet records. Fabricated hashes = immediate zero score + blacklist consideration.

### Schema Traps

**Attack:** Miner maintains stale Ledger, hopes validators don't notice.

**Defense:** Validators track recent schema changes across the metagraph. Challenges periodically require subnets that changed recently. Stale miners fail these traps.

```python
# Validator maintains list of recent changes
recent_changes = [
    {"subnet": "SN22", "changed": "2026-02-07", "field": "output_schema"},
    {"subnet": "SN13", "changed": "2026-02-06", "field": "input_schema"},
]

# 20% of challenges include a recently-changed subnet
if random() < 0.2:
    trap_subnet = random.choice(recent_changes)
    include_in_challenge(trap_subnet)
```

### Routing Replay

**Attack:** Miner always uses the same subnet routing regardless of task.

**Defense:** Validators issue diverse challenges. A miner who routes "find trending papers" the same as "analyze competitor pricing" is scored down on routing efficiency.

### Sybil Detection

**Attack:** Run multiple miners with identical Ledgers to capture more emissions.

**Defense:** Identical Ledger entries across UIDs trigger correlation analysis. Highly correlated miners see emission dilution.

---

## Validator Incentive Alignment

### V-Trust Mechanics

Validators earn based on consensus alignment:

```python
def validator_reward(validator, epoch_scores):
    consensus = stake_weighted_median(all_validator_scores)
    deviation = mean_absolute_error(validator.scores, consensus)
    v_trust = 1.0 - (deviation * 2.0)  # Penalize outliers
    return base_reward * max(0.5, v_trust)
```

### Why This Works

- **Honest validators converge** on similar scores (hash verification is deterministic, schema validation is deterministic)
- **Dishonest validators deviate** and lose V-Trust
- **Colluding validators** would need majority stake to shift consensus

---

## Cadence

| Event | Frequency |
|-------|-----------|
| Synthetic challenges | Every 20 blocks (~4 minutes) |
| Organic traffic | Real-time as requests arrive |
| Weight setting | Every 360 blocks (~1 hour) |
| Ledger trap injection | 20% of challenges |

---
