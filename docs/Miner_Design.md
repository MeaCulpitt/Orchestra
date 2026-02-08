# Orchestra: Miner Architecture & Operations

Orchestra miners are **Lead Architects** — they coordinate Bittensor subnets to complete complex objectives. They don't perform raw compute; they decompose tasks, route to specialists, and synthesize results.

Miners earn emissions through two activities:
1. **Orchestration (60%)** — Successfully completing multi-subnet projects
2. **Ledger contributions (40%)** — Updating the shared Subnet Registry

Both happen together: orchestration work naturally surfaces Ledger updates.

---

## The Two Jobs

### Job 1: Orchestration

When a challenge arrives:

1. **Decompose** the objective into discrete subtasks
2. **Consult** the Subnet Ledger for routing
3. **Execute** queries with hash-locked proofs
4. **Synthesize** outputs into target schema
5. **Deliver** structured result

### Job 2: Ledger Maintenance

While executing orchestration work:

1. **Detect** schema changes in subnet responses
2. **Propose** updates to the shared Ledger
3. **Earn** emission weight when validators verify proposals

Ledger coverage is demand-driven — miners maintain entries for subnets they actually use. Obscure subnets that nobody routes to may remain uncatalogued, and that's fine.

---

## Worked Example: Full Cycle

### Challenge Received

```json
{
  "challenge_id": "0x5c3b...",
  "objective": "Research decentralized compute providers and identify market gaps",
  "target_schema": {
    "competitors": [{"name": "str", "strengths": "list", "weaknesses": "list"}],
    "gaps": [{"gap": "str", "opportunity": "str"}],
    "recommendation": "str"
  },
  "deadline_ms": 25000
}
```

### Step 1: Consult Ledger

Miner queries the shared Subnet Ledger:

```python
# What subnets handle market research?
search_subnets = ledger.find(capability="web_search")
# → [SN22 Desearch]

scrape_subnets = ledger.find(capability="structured_extraction")
# → [SN13 Data Universe]

# Get schemas for routing
sn22_schema = ledger.get("SN22")
sn13_schema = ledger.get("SN13")
```

### Step 2: Decompose

```
Task 1: Search for provider information
  → Subnet: SN22 (Desearch)
  → Query: "decentralized compute Akash Render Golem 2026"

Task 2: Extract structured data from provider sites
  → Subnet: SN13 (Data Universe)  
  → Query: Scrape pricing pages

Task 3: Synthesize findings
  → Local or SN1 (Apex)
```

### Step 3: Execute

```python
async def execute():
    # Task 1: Search
    t1 = await query_subnet(
        subnet="SN22",
        payload={"query": "decentralized compute...", "max_results": 15}
    )
    # Hash proof: 0x7a3f...
    
    # Task 2: Scrape (parallel where possible)
    urls = extract_urls(t1.results)
    t2 = await query_subnet(
        subnet="SN13",
        payload={"urls": urls[:5], "fields": ["pricing", "features"]}
    )
    # Hash proof: 0x8b4e...
    
    # Task 3: Synthesize
    t3 = await synthesize(data=[t1, t2], target_schema=challenge.target_schema)
    
    return assemble_response(t1, t2, t3)
```

### Step 4: Detect Ledger Update

During execution, miner notices SN13 response includes a new field:

```python
# Expected (from Ledger):
{"data": [...], "errors": [...]}

# Actual response:
{"data": [...], "errors": [...], "extraction_confidence": 0.94}

# New field detected → propose Ledger update
```

### Step 5: Submit Response + Proposal

```json
{
  "challenge_id": "0x5c3b...",
  "task_pipeline": [
    {"subnet": "SN22", "hash": "0x7a3f...", "latency_ms": 310},
    {"subnet": "SN13", "hash": "0x8b4e...", "latency_ms": 920},
    {"subnet": "local", "hash": "0x9c5d...", "latency_ms": 380}
  ],
  "standardized_data": {
    "competitors": [...],
    "gaps": [...],
    "recommendation": "..."
  },
  "ledger_proposals": [
    {
      "subnet": "SN13",
      "update_type": "schema_addition",
      "path": "output_schema.extraction_confidence",
      "value": {"type": "float", "range": [0, 1]},
      "evidence_hash": "0x8b4e..."
    }
  ]
}
```

---

## The Subnet Ledger

The Ledger is a **shared network resource**, not a per-miner cache.

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SHARED LEDGER                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  MINERS ──── read/propose ────▶ LEDGER ◀──── verify ──── VALIDATORS
│                                    │                             │
│                                    │                             │
│                                    ▼                             │
│                            EXTERNAL USERS                        │
│                            (paid API access)                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Access Model

- **Miners:** Read and propose updates freely (part of the protocol)
- **Validators:** Read, verify, and commit updates (governance role)
- **External users:** Pay for API access (subscription or per-query)

The Ledger is free to use within Orchestra. External API access is a separate revenue stream.

### Entry Structure

```json
{
  "SN22": {
    "name": "Desearch",
    "description": "Web and social search",
    "capabilities": ["web_search", "news_search", "social_search"],
    "input_schema": {
      "query": {"type": "string", "required": true},
      "max_results": {"type": "integer", "default": 10, "max": 100}
    },
    "output_schema": {
      "results": {"type": "array", "items": "SearchResult"},
      "total_found": {"type": "integer"}
    },
    "endpoint": "Synapse.Desearch",
    "avg_latency_ms": 340,
    "p95_latency_ms": 890,
    "reliability": 0.97,
    "cost_per_query": 0.002,
    "last_verified": "2026-02-08T22:30:00Z",
    "version": "2.3.1",
    "verified_by": ["validator_1", "validator_7", "validator_12"]
  }
}
```

---

## Ledger Contribution Types

### 1. Schema Updates

Detecting changes to subnet APIs during orchestration work.

```json
{
  "type": "schema_update",
  "subnet_id": "SN13",
  "changes": [
    {"path": "output_schema.extraction_confidence", "old": null, "new": {"type": "float"}}
  ],
  "evidence_hash": "0x..."
}
```

**Weight:** Standard

### 2. New Subnet Discovery

First accurate catalogue of a subnet you route to.

```json
{
  "type": "new_subnet",
  "subnet_id": "SN142",
  "entry": {
    "name": "...",
    "capabilities": [...],
    "input_schema": {...},
    "output_schema": {...}
  },
  "evidence": {
    "probe_hash": "0x...",
    "sample_response": {...}
  }
}
```

**Weight:** 5x standard (discovery bonus)

### 3. Deprecation Detection

Identifying subnets that have gone offline or unreliable.

```json
{
  "type": "deprecation",
  "subnet_id": "SN87",
  "reason": "offline",
  "evidence": {
    "probe_attempts": 10,
    "success_rate": 0.0
  }
}
```

**Weight:** Standard

### 4. Metrics Updates

Updating latency, reliability, cost figures based on your calls.

**Weight:** Reduced (easier to verify)

---

## Performance Scoring

### Orchestration (60% of emissions)

| Component | Weight | Measurement |
|-----------|--------|-------------|
| Hash verification | 20% | All calls have valid proofs |
| Schema compliance | 15% | Output matches target_schema |
| Completeness | 10% | Required fields present |
| Routing efficiency | 10% | Optimal subnet selection |
| Latency | 5% | Faster than deadline |

### Ledger (40% of emissions)

| Component | Weight | Measurement |
|-----------|--------|-------------|
| Update accuracy | 20% | Proposals verified correct |
| Discovery | 10% | New subnets catalogued |
| Freshness | 5% | Catching schema changes promptly |
| Coverage | 5% | Breadth of subnets you maintain |

---

## Technical Requirements

### Hardware

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 4-core | 8-core |
| RAM | 16GB | 32GB |
| Storage | 50GB SSD | 100GB SSD |
| Network | 100Mbps | 1Gbps |

Orchestra mining is **coordination, not compute**. The bottleneck is network latency and routing logic, not processing power.

### Software

- Python 3.10+
- Bittensor SDK
- Async HTTP client (aiohttp/httpx)
- Pydantic for schema validation

---

## Economics

### Earning Emissions

Emissions depend on your combined score:

```
S_total = S_orchestration + S_ledger
W_miner = S_total / sum(all_miner_scores)
emissions = W_miner × block_emissions
```

Higher orchestration success rate + accurate Ledger contributions = higher emissions.

### Costs

| Cost | Amount | Notes |
|------|--------|-------|
| Subnet calls | 0.005-0.015 TAO/job | Varies by routing |
| Proposal stake | 0.0001 TAO | Refunded if valid |

### Break-Even

~50% orchestration success rate, assuming average Ledger contribution.

Failed orchestration = sunk subnet costs with no emissions.

---

## Operational Tips

### Routing Optimization

- Cache Ledger locally, sync frequently
- Track personal success rates per subnet
- Parallelize independent subtasks
- Have fallback subnets for critical capabilities

### Ledger Contribution Strategy

- Watch for schema mismatches during execution — that's your signal
- First to propose a valid update gets full credit
- Discovery bonuses are one-time — find new subnets before others do

### Risk Management

- Failed orchestration = sunk subnet costs
- False Ledger proposals = slashed stake
- Stale routing = lower success rate

Quality over quantity.

---
