# Orchestra: The Orchestration Layer for Bittensor

Orchestra coordinates Bittensor subnets to complete complex tasks. Instead of manually querying multiple subnets and synthesizing their outputs, you send Orchestra a high-level objective — it handles decomposition, routing, execution, and delivery.

One request in. Structured result out.

---

## The Problem

Bittensor has 100+ specialized subnets. Each does one thing well:
- SN22 (Desearch) searches the web
- SN1 (Apex) runs algorithmic competitions
- SN62 (Ridges) executes agent tasks
- SN13 (Data Universe) scrapes structured data
- SN64 (Chutes) runs inference

But real tasks require multiple subnets working together. Today, that means:

| Step | You do it manually |
|------|-------------------|
| 1 | Figure out which subnets you need |
| 2 | Learn each subnet's API/Synapse format |
| 3 | Query each subnet separately |
| 4 | Handle failures and retries |
| 5 | Reconcile different output formats |
| 6 | Synthesize into a coherent result |

This is the **Fragmentation Tax** — the overhead of coordinating decentralized intelligence.

---

## How Orchestra Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     ORCHESTRA PIPELINE                           │
├─────────────────────────────────────────────────────────────────┤
│  1. REQUEST         User submits high-level objective           │
│                     "Analyze competitor pricing and recommend   │
│                      a strategy for our inference API"          │
├─────────────────────────────────────────────────────────────────┤
│  2. DECOMPOSITION   Miner breaks objective into subnet tasks    │
│                     → Market data (SN22)                        │
│                     → Competitor scraping (SN13)                │
│                     → Strategic synthesis (SN1)                 │
├─────────────────────────────────────────────────────────────────┤
│  3. EXECUTION       Miner queries subnets, collects outputs     │
│                     Hash-locked proofs verify real calls        │
├─────────────────────────────────────────────────────────────────┤
│  4. SYNTHESIS       Miner aggregates and structures results     │
│                     Pydantic-validated JSON output              │
├─────────────────────────────────────────────────────────────────┤
│  5. DELIVERY        User receives structured, verified result   │
│                     Ready for downstream integration            │
└─────────────────────────────────────────────────────────────────┘
```

**Miners** are Lead Architects — they manage the project, not the compute.
**Validators** audit the work — verify subnet calls happened, check output quality.
**Users** get results — no coordination overhead.

---

## Worked Example: Competitive Analysis

### Request

```json
{
  "objective": "Analyze cloud GPU pricing from major providers and recommend positioning for a new inference API priced competitively against RunPod and Vast.ai",
  "target_schema": {
    "competitors": [{"name": "str", "pricing": "dict", "strengths": "list"}],
    "recommendation": {"price_point": "float", "rationale": "str"},
    "confidence": "float"
  }
}
```

### Miner Decomposition

```
Task 1: Market research
  → Subnet: SN22 (Desearch)
  → Query: "cloud GPU pricing RunPod Vast.ai Lambda Labs 2026"
  → Expected: Recent pricing data, market positioning

Task 2: Structured data extraction  
  → Subnet: SN13 (Data Universe)
  → Query: Scrape pricing pages for RunPod, Vast.ai, Lambda
  → Expected: Structured JSON with tiers, specs, prices

Task 3: Strategic synthesis
  → Subnet: SN1 (Apex) or high-reasoning model
  → Query: Synthesize findings into recommendation
  → Expected: Price point, rationale, confidence score
```

### Execution

| Step | Subnet | Query | Cost | Result |
|------|--------|-------|------|--------|
| 1 | SN22 | Web search | 0.002 TAO | 15 relevant articles |
| 2 | SN13 | Page scraping | 0.003 TAO | Structured pricing for 3 providers |
| 3 | SN1 | Synthesis | 0.004 TAO | Recommendation + rationale |

**Total subnet cost:** 0.009 TAO

### Delivery

```json
{
  "task_pipeline": [
    {"subnet": "SN22", "query": "...", "hash": "0x7a3f...", "latency_ms": 340},
    {"subnet": "SN13", "query": "...", "hash": "0x8b2c...", "latency_ms": 890},
    {"subnet": "SN1", "query": "...", "hash": "0x9d1e...", "latency_ms": 450}
  ],
  "standardized_data": {
    "competitors": [
      {"name": "RunPod", "pricing": {"a100_80gb": 1.99, "a40": 0.79}, "strengths": ["spot pricing", "templates"]},
      {"name": "Vast.ai", "pricing": {"a100_80gb": 1.45, "a40": 0.65}, "strengths": ["lowest price", "marketplace"]},
      {"name": "Lambda", "pricing": {"a100_80gb": 1.89, "a40": 0.99}, "strengths": ["reliability", "enterprise"]}
    ],
    "recommendation": {
      "price_point": 0.72,
      "rationale": "Position 10% below Vast.ai on A40 tier to capture price-sensitive users while maintaining margin above spot market volatility"
    },
    "confidence": 0.84
  },
  "final_synthesis": "Based on current market analysis, recommend $0.72/hr for A40-equivalent inference. This undercuts Vast.ai by 10% while remaining 15% above volatile spot pricing..."
}
```

**User cost:** 0.012 TAO (subnet costs + Orchestra margin)
**Miner earned:** 0.018 TAO (emissions) + 0.002 TAO (margin share)
**Time:** 2.1 seconds total

---

## Payment Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                      PAYMENT FLOW                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  USER                  ORCHESTRA              SUBNETS            │
│    │                      │                      │               │
│    │── Request + Fee ────▶│                      │               │
│    │   (0.012 TAO)        │                      │               │
│    │                      │                      │               │
│    │                      │── Query + Pay ──────▶│ SN22          │
│    │                      │   (0.002 TAO)        │               │
│    │                      │── Query + Pay ──────▶│ SN13          │
│    │                      │   (0.003 TAO)        │               │
│    │                      │── Query + Pay ──────▶│ SN1           │
│    │                      │   (0.004 TAO)        │               │
│    │                      │                      │               │
│    │                      │◀── Results ──────────│               │
│    │◀── Delivery ─────────│                      │               │
│                                                                  │
│  Subnet costs: 0.009 TAO                                        │
│  Orchestra margin: 0.003 TAO                                    │
│  → Miner share: 0.002 TAO                                       │
│  → Protocol: 0.001 TAO                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why Not Call Subnets Directly?

| Direct calls | Orchestra |
|--------------|-----------|
| You figure out which subnets to use | Miner figures it out |
| You learn each subnet's API | Standardized input/output |
| You handle different response formats | Pydantic-validated JSON |
| You synthesize outputs yourself | Miner synthesizes |
| You retry on failures | Miner handles reliability |
| You pay subnet costs only | Small premium for managed service |

**The tradeoff:** Your time and expertise vs. Orchestra's fee.

For developers building agents, the fee is worth it — one API call replaces hours of integration work.

---

## Documentation

| Document | Description |
|----------|-------------|
| [Incentive Mechanism](./docs/Incentive_Mechanism.md) | Scoring formula, emission split, anti-gaming |
| [Miner Architecture](./docs/Miner_Design.md) | Decomposition, execution, Ledger maintenance |
| [Validator Architecture](./docs/Validator_Design.md) | Audit methodology, scoring rubric |
| [Business Rationale](./docs/Business_Rationale.md) | Problem statement, competitive landscape |
| [Go-To-Market](./docs/Go_To_Market.md) | Target users, growth channels, incentives |

---

## The Subnet Ledger

To route tasks effectively, miners maintain a real-time registry of subnet capabilities:

```json
{
  "SN22": {
    "name": "Desearch",
    "capabilities": ["web_search", "social_search", "news"],
    "input_schema": {"query": "str", "max_results": "int"},
    "output_schema": {"results": "list[dict]", "metadata": "dict"},
    "avg_latency_ms": 350,
    "reliability": 0.97,
    "cost_per_query": 0.002
  },
  "SN13": {
    "name": "Data Universe", 
    "capabilities": ["web_scraping", "structured_extraction"],
    ...
  }
}
```

The Ledger is:
- **Continuously updated** by miners polling the metagraph
- **Validated** by validators through schema traps
- **Shared** as a network resource for routing optimization

---

## For Miners

Earn TAO by:
1. Receiving complex objectives from validators
2. Decomposing into optimal subnet routing
3. Executing queries with hash-locked proofs
4. Synthesizing and delivering structured results

### Unit Economics

| Scenario | Subnet costs | Emissions | Margin share | Net profit |
|----------|--------------|-----------|--------------|------------|
| Simple (2 subnets) | 0.005 TAO | 0.012 TAO | 0.002 TAO | +0.009 TAO |
| Complex (4 subnets) | 0.012 TAO | 0.022 TAO | 0.004 TAO | +0.014 TAO |
| Failed decomposition | 0.008 TAO | 0 TAO | 0 TAO | -0.008 TAO |

**Risk:** Bad routing = wasted subnet costs + zero emissions.
**Reward:** Good routing = emissions + margin share.

---

## For Validators

Earn dividends by:
1. Generating complex objectives (synthetic and organic)
2. Verifying hash proofs of subnet calls
3. Validating output against target schema
4. Scoring decomposition quality

---

## For Developers

Integrate Orchestra to:
- Complete multi-step tasks with one API call
- Receive structured, validated JSON
- Skip subnet integration overhead
- Build agents that leverage the full metagraph

---

## License

MIT

---
