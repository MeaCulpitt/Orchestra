# Orchestra: The Orchestration Layer for Bittensor

Orchestra completes complex tasks by coordinating Bittensor subnets. Submit a high-level objective, receive a structured result. Miners handle decomposition, routing, execution, and synthesis.

One request in. Verified result out.

---

## The Problem

Bittensor has 100+ specialized subnets. Using them together is hard:

- **Which subnet does what?** No canonical registry.
- **Different APIs and formats.** Each subnet is its own integration.
- **Complex tasks need multiple subnets.** Manual coordination doesn't scale.
- **Reliability varies.** Schemas change, subnets go offline.

This is the **Fragmentation Tax** — the overhead that prevents Bittensor from being used as a unified intelligence layer.

---

## How Orchestra Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     ORCHESTRA PIPELINE                           │
├─────────────────────────────────────────────────────────────────┤
│  1. REQUEST         You submit a high-level objective           │
│                     "Analyze competitor pricing and recommend   │
│                      positioning for our inference API"         │
├─────────────────────────────────────────────────────────────────┤
│  2. DECOMPOSITION   Miner breaks objective into subnet tasks    │
│                     → Market data (SN22 Desearch)               │
│                     → Competitor scraping (SN13 Data Universe)  │
│                     → Strategic synthesis (SN1 Apex)            │
├─────────────────────────────────────────────────────────────────┤
│  3. EXECUTION       Miner queries subnets, collects outputs     │
│                     Hash-locked proofs verify real calls        │
├─────────────────────────────────────────────────────────────────┤
│  4. SYNTHESIS       Miner aggregates into structured result     │
│                     Pydantic-validated against your schema      │
├─────────────────────────────────────────────────────────────────┤
│  5. DELIVERY        You receive verified, structured output     │
│                     Ready for downstream integration            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Worked Example

### Your Request

```json
{
  "objective": "Research cloud GPU pricing from RunPod, Vast.ai, and Lambda. Recommend a price point for our new inference API.",
  "target_schema": {
    "competitors": [{"name": "str", "pricing": "dict", "strengths": "list"}],
    "recommendation": {"price_point": "float", "rationale": "str"}
  }
}
```

### What You Get Back

```json
{
  "competitors": [
    {"name": "RunPod", "pricing": {"a100_80gb": 1.99}, "strengths": ["spot pricing", "templates"]},
    {"name": "Vast.ai", "pricing": {"a100_80gb": 1.45}, "strengths": ["lowest price", "marketplace"]},
    {"name": "Lambda", "pricing": {"a100_80gb": 1.89}, "strengths": ["reliability", "enterprise"]}
  ],
  "recommendation": {
    "price_point": 0.72,
    "rationale": "Position 10% below Vast.ai on A40 tier. Captures price-sensitive users while maintaining margin above spot volatility."
  }
}
```

**Time:** 2.3 seconds
**Cost:** 0.012 TAO
**Your integration work:** Zero

---

## Why Not Call Subnets Directly?

| Direct Integration | Orchestra |
|--------------------|-----------|
| You figure out which subnets to use | Miner figures it out |
| You learn each subnet's API | Standardized input/output |
| You handle different response formats | Pydantic-validated JSON |
| You synthesize outputs yourself | Miner synthesizes |
| You retry on failures | Miner handles reliability |
| You track schema changes | Network maintains registry |

**The tradeoff:** Your engineering time vs. Orchestra's fee.

---

## The Subnet Ledger

To route effectively, Orchestra maintains a shared registry of subnet capabilities — the **Subnet Ledger**.

This isn't just internal infrastructure. It's a network resource:

- **Miners** read it for routing decisions
- **Miners** update it when they discover changes during orchestration
- **Validators** verify updates against live subnets
- **External users** can query it via paid API

If you don't need full orchestration but want to know what SN22 accepts and returns, query the Ledger.

---

## Documentation

| Document | Description |
|----------|-------------|
| [Incentive Mechanism](./docs/Incentive_Mechanism.md) | 60/40 split: orchestration + Ledger contributions |
| [Miner Architecture](./docs/Miner_Design.md) | Task execution, Ledger maintenance |
| [Validator Architecture](./docs/Validator_Design.md) | Verification methodology |
| [Business Rationale](./docs/Business_Rationale.md) | Problem statement, revenue model |
| [Go-To-Market](./docs/Go_To_Market.md) | Target customers, growth strategy |

---

## For Developers

```python
from orchestra import Client

client = Client(api_key="...")

result = client.execute(
    objective="Find trending AI papers and summarize key contributions",
    target_schema={
        "papers": [{"title": "str", "summary": "str"}],
        "synthesis": "str"
    }
)

# result is Pydantic-validated, ready to use
print(result.papers[0].title)
```

---

## For Miners

Earn TAO by:
1. Completing multi-subnet orchestration jobs (60% of emissions)
2. Contributing accurate updates to the Subnet Ledger (40% of emissions)

Better routing = higher success rate = more emissions.

---

## For Validators

Earn dividends by:
1. Verifying miner execution (hash proofs, schema compliance)
2. Validating Ledger updates against live subnets

---

## License

MIT

---
