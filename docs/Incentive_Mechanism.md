# Orchestra: Incentive & Mechanism Design

Orchestra rewards two types of work:

1. **Orchestration (60% of emissions)** — Successfully completing multi-subnet projects
2. **Ledger Contributions (40% of emissions)** — Maintaining the shared Subnet Registry

Both activities happen together: orchestration work naturally surfaces Ledger updates.

---

## Emission Split: 60/40

### Orchestration (60%)

Rewards miners for completing complex objectives:

| Component | Weight | Measurement |
|-----------|--------|-------------|
| Hash verification | 20% | All subnet calls have valid on-chain proofs |
| Schema compliance | 15% | Output matches target_schema |
| Completeness | 10% | Required fields present and populated |
| Routing efficiency | 10% | Optimal subnet selection |
| Latency | 5% | Faster than deadline |

### Ledger Contributions (40%)

Rewards miners for maintaining the shared registry:

| Component | Weight | Measurement |
|-----------|--------|-------------|
| Update accuracy | 20% | Proposed changes verified as correct |
| Discovery | 10% | New subnets catalogued first |
| Freshness | 5% | Detecting stale entries |
| Coverage | 5% | Breadth of subnets maintained |

---

## Worked Example: Scoring a Response

### Scenario

Miner receives orchestration challenge and notices a schema change during execution.

### Orchestration Task

```json
{
  "objective": "Find trending AI research papers and summarize key findings",
  "target_schema": {
    "papers": [{"title": "str", "summary": "str", "impact": "str"}],
    "synthesis": "str"
  }
}
```

### Execution

1. **Query SN22 (Desearch)** for paper search → Success, hash `0x7a3f...`
2. **Query SN13 (Data Universe)** for abstract extraction → Success, hash `0x8b4e...`
3. **Notice:** SN13 response includes new field `extraction_confidence` not in Ledger
4. **Synthesize** results into target schema
5. **Submit:** Orchestration response + Ledger update proposal

### Orchestration Scoring

| Component | Score | Calculation |
|-----------|-------|-------------|
| Hash verification | 1.0 | Both calls verified |
| Schema compliance | 1.0 | Output passes validation |
| Completeness | 1.0 | All fields present |
| Routing efficiency | 0.9 | Good choices, minor optimization possible |
| Latency | 1.0 | Under deadline |
| **Orchestration total** | 0.59 | (0.20×1.0)+(0.15×1.0)+(0.10×1.0)+(0.10×0.9)+(0.05×1.0) |

### Ledger Contribution Scoring

```json
{
  "proposal": {
    "subnet": "SN13",
    "update_type": "schema_addition",
    "path": "output_schema.extraction_confidence",
    "value": {"type": "float", "range": [0, 1]},
    "evidence_hash": "0x8b4e..."
  }
}
```

Validator verifies:
1. Calls SN13 directly
2. Confirms `extraction_confidence` field exists
3. Confirms type and range are correct
4. **Approves update**

| Component | Score | Calculation |
|-----------|-------|-------------|
| Update accuracy | 1.0 | Proposal verified correct |
| Discovery | 0.5 | Not new subnet, but new field |
| Freshness | 1.0 | Caught change within 24 hours |
| Coverage | N/A | Not applicable this round |
| **Ledger total** | 0.30 | (0.20×1.0)+(0.10×0.5)+(0.05×1.0)+(0.05×0) |

### Combined Score

```
S_total = S_orchestration + S_ledger
        = 0.59 + 0.30
        = 0.89
```

---

## Ledger Contribution Types

### 1. New Subnet Discovery

First miner to accurately catalogue a new subnet.

```json
{
  "proposal": {
    "type": "new_subnet",
    "subnet_id": "SN142",
    "entry": {
      "name": "NewSubnet",
      "description": "...",
      "capabilities": ["..."],
      "input_schema": {...},
      "output_schema": {...}
    },
    "evidence": {
      "probe_hash": "0x...",
      "sample_response": {...}
    }
  }
}
```

**Reward:** 5x normal contribution weight (one-time)

### 2. Schema Updates

Detecting and proposing changes to existing subnet schemas.

```json
{
  "proposal": {
    "type": "schema_update",
    "subnet_id": "SN22",
    "changes": [
      {"path": "output_schema.results.snippet", "old": "str", "new": "str | null"},
      {"path": "input_schema.max_results.max", "old": 100, "new": 50}
    ],
    "evidence_hash": "0x..."
  }
}
```

**Reward:** Standard contribution weight

### 3. Deprecation Detection

Identifying subnets that are offline, unreliable, or deprecated.

```json
{
  "proposal": {
    "type": "deprecation",
    "subnet_id": "SN87",
    "reason": "offline",
    "evidence": {
      "probe_attempts": 10,
      "success_rate": 0.0,
      "last_success": "2026-01-15T..."
    }
  }
}
```

**Reward:** Standard contribution weight

### 4. Metrics Updates

Updating latency, reliability, and cost figures.

**Reward:** Reduced weight (easier to verify)

---

## Ledger Governance

The Ledger is a shared resource. Updates require validation.

### Proposal → Verification → Commit

```
┌─────────────────────────────────────────────────────────────────┐
│                  LEDGER UPDATE FLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  MINER                 VALIDATORS              LEDGER            │
│    │                       │                      │              │
│    │── Propose update ────▶│                      │              │
│    │                       │── Verify against ───▶│ (test call)  │
│    │                       │   live subnet        │              │
│    │                       │◀── Result ───────────│              │
│    │                       │                      │              │
│    │                       │── If valid: ────────▶│ Commit       │
│    │                       │                      │              │
│    │                       │── If invalid: ──────▶│ Reject       │
│    │◀── Stake slashed ─────│                      │              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Conflict Resolution

Multiple miners might propose the same update:

```python
def resolve_conflict(proposals):
    # Sort by timestamp (first proposer wins)
    sorted_proposals = sorted(proposals, key=lambda p: p.timestamp)
    
    # Verify first proposal
    if verify(sorted_proposals[0]):
        # First miner gets full credit
        credit(sorted_proposals[0].miner, weight=FULL_WEIGHT)
        
        # Others get reduced "confirmation" credit
        for p in sorted_proposals[1:]:
            if verify(p):
                credit(p.miner, weight=CONFIRMATION_WEIGHT)
    else:
        # First proposal invalid, try next
        resolve_conflict(sorted_proposals[1:])
```

### Anti-Spam

Proposals cost a small stake:

```python
PROPOSAL_STAKE = 0.0001  # TAO

def submit_proposal(miner, proposal):
    # Lock stake
    lock_stake(miner, PROPOSAL_STAKE)
    
    # Queue for verification
    queue_proposal(proposal)
    
    # After verification:
    if proposal.verified:
        unlock_stake(miner)
        # Miner's Ledger contribution score increases
    else:
        slash_stake(miner, PROPOSAL_STAKE * 0.5)
        unlock_stake(miner, PROPOSAL_STAKE * 0.5)
```

False proposals lose half their stake.

---

## Scoring Formulas

### Orchestration Score

```
S_orch = (0.20 × hash_verified) + 
         (0.15 × schema_valid) + 
         (0.10 × completeness) + 
         (0.10 × routing_score) + 
         (0.05 × latency_score)
```

All components are 0.0 to 1.0.

### Ledger Score

```
S_ledger = (0.20 × update_accuracy) + 
           (0.10 × discovery_score) + 
           (0.05 × freshness_score) + 
           (0.05 × coverage_score)
```

### Combined Score

```
S_total = S_orch + S_ledger

# Normalized for weight setting
W_miner = S_total / sum(all_miner_scores)
```

---

## Miner Economics

### Costs

| Cost | Amount | Notes |
|------|--------|-------|
| Subnet calls | 0.005-0.015 TAO | Per orchestration job |
| Proposal stake | 0.0001 TAO | Refunded if valid |

### Profitability

Depends on:
- Orchestration success rate (higher = more emissions)
- Ledger contribution accuracy (verified updates earn weight)
- Subnet call costs (efficient routing = lower costs)

Break-even requires ~50% orchestration success rate.

---

## Anti-Gaming Mechanisms

### Hash Fabrication

**Attack:** Claim subnet calls without making them.

**Defense:** Validators cross-reference hashes against subnet transaction logs. Fabricated hashes = zero score + blacklist.

### Ledger Spam

**Attack:** Flood proposals to farm emissions.

**Defense:** Proposal stake + slash on invalid. Spam is economically irrational.

### Stale Copying

**Attack:** Copy other miners' Ledger updates.

**Defense:** Timestamp priority. First proposer gets full credit; copiers get nothing or confirmation bonus only.

### Collusion

**Attack:** Miners and validators collude to approve false updates.

**Defense:** 
- Multiple validators must agree
- Random validators selected per proposal
- External users can challenge entries (with stake)

### Orchestration Shortcuts

**Attack:** Skip synthesis, just concatenate subnet outputs.

**Defense:** Schema compliance check. Raw concatenation won't match target schema structure.

---

## Validator Incentives

Validators earn by:
1. Verifying orchestration hash proofs
2. Testing Ledger proposals against live subnets
3. Maintaining consensus on miner scores

### V-Trust Mechanics

```python
def update_v_trust(validator, epoch):
    consensus = stake_weighted_median(all_validator_scores)
    deviation = mean_absolute_error(validator.scores, consensus)
    
    # Ledger verification accuracy
    ledger_accuracy = validator.correct_verifications / validator.total_verifications
    
    # Combined trust score
    v_trust = (0.7 * (1 - deviation)) + (0.3 * ledger_accuracy)
    
    return v_trust
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
