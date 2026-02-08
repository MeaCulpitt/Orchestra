# Orchestra: Orchestration Layer + Subnet Registry for Bittensor

Orchestra provides two products:

1. **Managed Intelligence** — Submit complex objectives, receive structured results. Miners coordinate multiple subnets on your behalf.

2. **The Subnet Ledger** — The canonical, validated registry of every Bittensor subnet's capabilities, schemas, and endpoints. One API for subnet discovery.

Both products reinforce each other: orchestration work generates Ledger updates; the Ledger enables better orchestration.

---

## The Problem

Bittensor has 100+ specialized subnets. Using them is hard:

| Challenge | Impact |
|-----------|--------|
| **Discovery** | Which subnet does what? No central registry. |
| **Integration** | Each subnet has different APIs, schemas, formats. |
| **Coordination** | Complex tasks require multiple subnets working together. |
| **Reliability** | Schema changes break integrations. No freshness guarantees. |

For developers building agents or applications on Bittensor, this is the **Fragmentation Tax** — hours spent on integration instead of product.

---

## Product 1: Managed Intelligence

Submit a high-level objective. Orchestra handles decomposition, routing, execution, and synthesis.

```
┌─────────────────────────────────────────────────────────────────┐
│                   MANAGED INTELLIGENCE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  YOU                      ORCHESTRA                SUBNETS       │
│   │                          │                        │          │
│   │── "Analyze competitor ──▶│                        │          │
│   │    pricing and           │── Query ──────────────▶│ SN22     │
│   │    recommend strategy"   │── Query ──────────────▶│ SN13     │
│   │                          │── Query ──────────────▶│ SN1      │
│   │                          │◀── Results ────────────│          │
│   │◀── Structured report ────│                        │          │
│   │    (Pydantic-validated)  │                        │          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**You get:** Structured, validated results. No subnet integration work.

**You pay:** Per-project fee (covers subnet costs + margin).

---

## Product 2: The Subnet Ledger

The canonical registry of Bittensor subnet capabilities. Validated, versioned, always current.

```json
{
  "SN22": {
    "name": "Desearch",
    "description": "Web and social search",
    "capabilities": ["web_search", "news_search", "social_search"],
    "input_schema": {
      "query": {"type": "string", "required": true},
      "max_results": {"type": "integer", "default": 10}
    },
    "output_schema": {
      "results": {"type": "array", "items": "SearchResult"},
      "total_found": {"type": "integer"}
    },
    "endpoint": "Synapse.Desearch",
    "avg_latency_ms": 340,
    "reliability": 0.97,
    "cost_per_query": 0.002,
    "last_verified": "2026-02-08T22:30:00Z",
    "version": "2.3.1"
  }
}
```

**Use cases:**

| Customer | Use Case |
|----------|----------|
| Agent frameworks | Route tasks to correct subnets |
| LLM applications | Tool-use with Bittensor backends |
| Developers | Discover and integrate subnets |
| Other subnets | Cross-subnet coordination |

**You get:** Verified schemas, real-time accuracy, single API.

**You pay:** Per-lookup or subscription.

---

## Why Both Products?

They create a flywheel:

```
┌─────────────────────────────────────────────────────────────────┐
│                      THE FLYWHEEL                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Orchestration jobs ──▶ Miners call subnets ──▶ Ledger updates │
│         ▲                                              │         │
│         │                                              ▼         │
│   Better routing ◀──── Accurate Ledger ◀──── Verification       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

- Every orchestration job tests subnet schemas → Ledger gets fresher
- Fresher Ledger → better routing decisions → better orchestration
- Both products share infrastructure costs

---

## Worked Example: Full Cycle

### User Request (Orchestration)

```json
{
  "objective": "Research cloud GPU pricing and recommend positioning for our inference API",
  "target_schema": {
    "competitors": [{"name": "str", "pricing": "dict"}],
    "recommendation": {"price_point": "float", "rationale": "str"}
  }
}
```

### Miner Execution

1. **Consult Ledger:** Which subnets handle market research? → SN22 (search), SN13 (scraping)
2. **Execute queries:** Call SN22 and SN13 with hash-locked proofs
3. **Verify schemas:** Do responses match Ledger entries? If not, submit Ledger update
4. **Synthesize:** Aggregate results into target schema
5. **Deliver:** Return structured response + Ledger update proposals

### Ledger Update (Byproduct)

Miner noticed SN13 added a new field to its output:

```json
{
  "subnet": "SN13",
  "update_type": "schema_change",
  "field": "output_schema.metadata.scrape_timestamp",
  "old_value": null,
  "new_value": {"type": "string", "format": "iso8601"},
  "evidence_hash": "0x7a3f...",
  "proposed_by": "miner_uid_42"
}
```

### Validator Verification

1. Validator calls SN13 directly
2. Confirms new field exists
3. Approves Ledger update
4. Miner earns Ledger contribution reward

---

## The Ledger as Network Infrastructure

The Ledger isn't just Orchestra's internal cache — it's a **shared network resource**:

### On-Chain Registry

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEDGER ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  MINERS              SHARED LEDGER              VALIDATORS       │
│    │                      │                         │            │
│    │── Propose update ───▶│                         │            │
│    │                      │◀── Verify against ──────│            │
│    │                      │    live subnet          │            │
│    │                      │                         │            │
│    │◀── Read for routing ─│                         │            │
│    │                      │                         │            │
│  EXTERNAL USERS           │                         │            │
│    │                      │                         │            │
│    │◀── Query via API ────│                         │            │
│    │    (paid access)     │                         │            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Access Tiers

| Tier | Access | Price |
|------|--------|-------|
| **Free** | Subnet list, names, basic descriptions | 0 |
| **Developer** | Full schemas, 1000 lookups/month | 0.1 TAO/month |
| **Production** | Unlimited lookups, webhooks for changes | 1 TAO/month |
| **Enterprise** | SLA, dedicated support, custom integrations | Custom |

---

## Moat: Why Not Just Scrape It Yourself?

Anyone can poll the metagraph. Orchestra provides:

| DIY | Orchestra Ledger |
|-----|------------------|
| Raw subnet list | Validated, tested schemas |
| Self-reported capabilities | Verified via actual calls |
| Point-in-time snapshot | Real-time with change tracking |
| Your maintenance burden | Continuously updated by miners |
| Unknown reliability | Reliability scores, latency metrics |
| No SLA | Accuracy guarantees |

**The value isn't the data — it's the trust layer.**

---

## Documentation

| Document | Description |
|----------|-------------|
| [Incentive Mechanism](./docs/Incentive_Mechanism.md) | Dual rewards: orchestration + Ledger contributions |
| [Miner Architecture](./docs/Miner_Design.md) | Orchestration execution, Ledger updates |
| [Validator Architecture](./docs/Validator_Design.md) | Verification methodology, Ledger governance |
| [Business Rationale](./docs/Business_Rationale.md) | Dual-product strategy, revenue model |
| [Go-To-Market](./docs/Go_To_Market.md) | Target customers, growth channels |

---

## Revenue Model

| Product | Revenue Source | Flow |
|---------|----------------|------|
| Orchestration | Per-project fees | User → Orchestra → Subnets |
| Ledger | Subscriptions + per-query | User → Orchestra |
| Ledger Enterprise | Licensing to agent frameworks | Platform → Orchestra |

Both products generate emissions for miners and validators.

---

## For Miners

Earn TAO through:

1. **Orchestration work** — Execute multi-subnet projects
2. **Ledger contributions** — Discover new subnets, update schemas, maintain accuracy

| Activity | Reward |
|----------|--------|
| Successful orchestration job | Emissions + margin share |
| New subnet discovered | Discovery bonus |
| Schema update accepted | Contribution reward |
| High Ledger accuracy | Accuracy multiplier |

---

## For Validators

Earn dividends through:

1. **Orchestration verification** — Confirm hash proofs, validate outputs
2. **Ledger governance** — Verify proposed updates, reject stale/false entries

---

## For Developers

**Using Orchestration:**
```python
from orchestra import OrchestraClient

client = OrchestraClient(api_key="...")
result = client.execute(
    objective="Analyze competitor pricing...",
    target_schema=MySchema
)
# result is Pydantic-validated, ready to use
```

**Using the Ledger:**
```python
from orchestra import LedgerClient

ledger = LedgerClient(api_key="...")

# Discover subnets by capability
search_subnets = ledger.find(capability="web_search")

# Get full schema for integration
schema = ledger.get_schema("SN22")

# Subscribe to changes
ledger.on_change("SN22", callback=handle_schema_update)
```

---

## License

MIT

---
