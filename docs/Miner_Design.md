# Orchestra: Miner Architecture & Operations

Orchestra miners are **Lead Architects** — project managers who coordinate Bittensor subnets to complete complex objectives. They don't perform raw compute; they decompose tasks, route to specialists, and synthesize results.

---

## What Miners Do

When a user or validator submits a complex objective, the miner:

1. **Decomposes** the objective into discrete subtasks
2. **Routes** each subtask to the optimal subnet
3. **Executes** queries with hash-locked proofs
4. **Synthesizes** outputs into a structured deliverable

The miner earns emissions based on coordination quality (70%) and Ledger accuracy (30%).

---

## Worked Example: End-to-End Task Execution

### Challenge Received

```json
{
  "challenge_id": "0x4f2a...",
  "objective": "Research the competitive landscape for decentralized compute marketplaces and identify gaps our product could fill",
  "target_schema": {
    "competitors": [{"name": "str", "description": "str", "strengths": "list", "weaknesses": "list"}],
    "market_gaps": [{"gap": "str", "opportunity": "str", "difficulty": "str"}],
    "recommendation": "str"
  },
  "deadline_ms": 30000
}
```

### Step 1: Decomposition

Miner's reasoning (internal):

```
Objective analysis:
- Need current market data → web search
- Need structured competitor info → data extraction
- Need strategic analysis → synthesis/reasoning

Decomposition:
1. Search for decentralized compute providers (SN22 Desearch)
2. Scrape competitor websites for features/pricing (SN13 Data Universe)
3. Search for market analysis/reports (SN22 Desearch)
4. Synthesize findings into strategic recommendation (SN1 Apex or local model)

Estimated cost: 0.011 TAO
Estimated time: 4-8 seconds
```

### Step 2: Ledger Lookup

Miner consults internal Subnet Ledger:

```json
{
  "SN22": {
    "name": "Desearch",
    "capabilities": ["web_search", "news_search", "social_search"],
    "input_schema": {"query": "str", "max_results": "int", "search_type": "str"},
    "output_schema": {"results": "list[dict]", "total_found": "int"},
    "avg_latency_ms": 340,
    "reliability": 0.97,
    "cost_per_query": 0.002,
    "last_updated": "2026-02-08T10:00:00Z"
  },
  "SN13": {
    "name": "Data Universe",
    "capabilities": ["web_scraping", "structured_extraction", "pdf_parsing"],
    "input_schema": {"urls": "list[str]", "extract_fields": "list[str]"},
    "output_schema": {"data": "list[dict]", "errors": "list"},
    "avg_latency_ms": 890,
    "reliability": 0.92,
    "cost_per_query": 0.003,
    "last_updated": "2026-02-08T09:30:00Z"
  }
}
```

### Step 3: Execution

```python
async def execute_pipeline(objective, deadline):
    results = {}
    
    # Task 1: Market search
    t1 = await query_subnet(
        subnet="SN22",
        payload={"query": "decentralized compute marketplace Akash Render Golem 2026", "max_results": 20},
    )
    results["market_search"] = t1
    
    # Task 2: Competitor scraping (parallel with Task 3)
    competitor_urls = extract_urls(t1.results)
    t2 = query_subnet(
        subnet="SN13",
        payload={"urls": competitor_urls[:5], "extract_fields": ["pricing", "features", "about"]},
    )
    
    # Task 3: Analysis search (parallel with Task 2)
    t3 = query_subnet(
        subnet="SN22", 
        payload={"query": "decentralized compute market analysis report", "max_results": 10},
    )
    
    results["competitor_data"], results["analysis"] = await asyncio.gather(t2, t3)
    
    # Task 4: Synthesis
    t4 = await synthesize(
        data=results,
        target_schema=objective.target_schema,
        instruction="Identify market gaps and strategic opportunities"
    )
    results["synthesis"] = t4
    
    return results
```

### Step 4: Response Assembly

```json
{
  "challenge_id": "0x4f2a...",
  "task_pipeline": [
    {
      "step": 1,
      "subnet": "SN22",
      "task": "market_search",
      "query": {"query": "decentralized compute...", "max_results": 20},
      "hash": "0x7a3f8c2d...",
      "latency_ms": 320,
      "cost": 0.002
    },
    {
      "step": 2,
      "subnet": "SN13", 
      "task": "competitor_scraping",
      "query": {"urls": ["https://akash.network", "..."], "extract_fields": ["..."]},
      "hash": "0x8b4e1f9a...",
      "latency_ms": 1240,
      "cost": 0.003
    },
    {
      "step": 3,
      "subnet": "SN22",
      "task": "analysis_search",
      "query": {"query": "decentralized compute market analysis...", "max_results": 10},
      "hash": "0x9c5d2e8b...",
      "latency_ms": 290,
      "cost": 0.002
    },
    {
      "step": 4,
      "subnet": "local",
      "task": "synthesis",
      "hash": "0xa6f3c7d1...",
      "latency_ms": 450,
      "cost": 0.000
    }
  ],
  "standardized_data": {
    "competitors": [
      {
        "name": "Akash Network",
        "description": "Decentralized cloud compute marketplace",
        "strengths": ["Low pricing", "Kubernetes native", "Active community"],
        "weaknesses": ["Limited GPU availability", "Complex onboarding"]
      },
      {
        "name": "Render Network",
        "description": "Distributed GPU rendering",
        "strengths": ["Strong GPU network", "Creator focused"],
        "weaknesses": ["Rendering-specific", "Limited general compute"]
      },
      // ... more competitors
    ],
    "market_gaps": [
      {
        "gap": "No dominant player for ML inference workloads",
        "opportunity": "Purpose-built inference routing with latency guarantees",
        "difficulty": "Medium - requires validator network for SLA enforcement"
      },
      {
        "gap": "Poor developer experience across all platforms",
        "opportunity": "One-click deployment with familiar interfaces",
        "difficulty": "Low - mostly UX investment"
      }
    ],
    "recommendation": "Focus on ML inference workloads with latency SLAs. Current market is fragmented between rendering (Render), general compute (Akash), and storage (Filecoin). No player owns inference. Enter with superior DX and measurable performance guarantees."
  },
  "final_synthesis": "The decentralized compute market has three established players but remains fragmented by use case...",
  "total_cost": 0.007,
  "total_latency_ms": 2300
}
```

---

## The Subnet Ledger

The Ledger is the miner's internal registry of subnet capabilities. Without an accurate Ledger, routing fails.

### Ledger Structure

```json
{
  "subnet_id": {
    "name": "Human readable name",
    "capabilities": ["list", "of", "capabilities"],
    "input_schema": { "pydantic": "schema" },
    "output_schema": { "pydantic": "schema" },
    "avg_latency_ms": 000,
    "p95_latency_ms": 000,
    "reliability": 0.00,
    "cost_per_query": 0.000,
    "last_updated": "ISO timestamp",
    "notes": "Optional operational notes"
  }
}
```

### Ledger Maintenance

Miners must continuously update their Ledger:

```python
async def maintain_ledger():
    while True:
        for subnet in TRACKED_SUBNETS:
            # Poll metagraph for subnet state
            state = await fetch_subnet_state(subnet)
            
            # Test current schema with probe query
            probe_result = await probe_subnet(subnet)
            
            # Update Ledger entry
            ledger[subnet] = {
                "name": state.name,
                "capabilities": infer_capabilities(probe_result),
                "input_schema": extract_input_schema(state),
                "output_schema": extract_output_schema(probe_result),
                "avg_latency_ms": state.metrics.avg_latency,
                "reliability": state.metrics.success_rate,
                "cost_per_query": state.pricing.per_query,
                "last_updated": datetime.utcnow().isoformat()
            }
        
        await asyncio.sleep(300)  # Update every 5 minutes
```

### Ledger Bootstrap

New miners can bootstrap their Ledger:

**Phase 1: Seed from network**
- Download published Ledger snapshots from top miners
- Verify against live probes

**Phase 2: Extend coverage**
- Probe subnets not in seed Ledger
- Earn discovery bonuses for new accurate entries

**Phase 3: Maintain freshness**
- Continuous polling for schema changes
- Validator traps penalize stale entries

---

## Input/Output Specification

### Input Format (Validator → Miner)

```python
class OrchestraSynapse(bt.Synapse):
    # Challenge identification
    challenge_id: str
    
    # The high-level objective
    objective: str
    
    # Required output structure
    target_schema: dict
    
    # Time limit
    deadline_ms: int = 30000
    
    # Optional hints (for synthetic challenges)
    hints: Optional[dict] = None
```

### Output Format (Miner → Validator)

```python
class OrchestraResponse(bt.Synapse):
    # Echo challenge ID
    challenge_id: str
    
    # Execution log with hash proofs
    task_pipeline: List[TaskStep]
    
    # Structured result matching target_schema
    standardized_data: dict
    
    # Human-readable summary
    final_synthesis: str
    
    # Metadata
    total_cost: float
    total_latency_ms: int
    ledger_version: str

class TaskStep(BaseModel):
    step: int
    subnet: str
    task: str
    query: dict
    hash: str  # On-chain transaction hash
    latency_ms: int
    cost: float
    error: Optional[str] = None
```

---

## Performance Dimensions

| Dimension | Weight | What's Measured |
|-----------|--------|-----------------|
| **Hash verification** | 25% | All subnet calls have valid on-chain proofs |
| **Schema compliance** | 20% | Output matches target_schema |
| **Completeness** | 15% | Required fields present and populated |
| **Routing efficiency** | 10% | Optimal subnet selection for task |
| **Ledger freshness** | 15% | Schema entries match live subnet state |
| **Ledger coverage** | 10% | Number of subnets accurately tracked |
| **Trap performance** | 5% | Success on validator schema traps |

---

## Technical Requirements

### Compute

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 4-core | 8-core |
| RAM | 16GB | 32GB |
| Storage | 50GB SSD | 100GB SSD |
| Network | 100Mbps | 1Gbps |

Orchestra mining is **not compute-intensive**. The bottleneck is coordination logic and network latency, not raw processing.

### Software

- Python 3.10+
- Bittensor SDK
- Async HTTP client (aiohttp/httpx)
- Pydantic for schema validation
- Local database for Ledger (SQLite/Redis)

### Network

- Low latency to major subnet validators
- Ability to make concurrent outbound requests
- Stable connection (reliability affects TWF-equivalent reputation)

---

## Operational Best Practices

### Decomposition Strategy

**Good decomposition:**
- Minimizes subnet calls while covering all requirements
- Parallelizes independent tasks
- Uses cheapest adequate subnet for each subtask

**Bad decomposition:**
- Sequential calls when parallel is possible
- Premium subnets for simple tasks
- Redundant calls "just in case"

### Error Handling

```python
async def query_with_retry(subnet, payload, max_retries=2):
    for attempt in range(max_retries + 1):
        try:
            result = await query_subnet(subnet, payload)
            return result
        except SubnetTimeout:
            if attempt < max_retries:
                await asyncio.sleep(0.5 * (attempt + 1))
                continue
            # Fall back to alternative subnet if available
            alt = get_alternative_subnet(subnet)
            if alt:
                return await query_subnet(alt, payload)
            raise
```

### Cost Optimization

- Cache frequently-used subnet responses (with TTL)
- Batch similar queries when subnet supports it
- Track cost-per-task to optimize routing decisions

---

## Unit Economics

### Revenue Model

| Source | Per Challenge | Daily (100 challenges) |
|--------|---------------|------------------------|
| Emissions | ~0.015 TAO | ~1.5 TAO |
| Margin share (organic) | ~0.002 TAO | ~0.2 TAO |
| **Total revenue** | ~0.017 TAO | ~1.7 TAO |

### Cost Model

| Cost | Per Challenge | Daily (100 challenges) |
|------|---------------|------------------------|
| Subnet calls (avg 3) | ~0.008 TAO | ~0.8 TAO |
| Compute | Negligible | ~0.01 TAO |
| **Total cost** | ~0.008 TAO | ~0.81 TAO |

### Profitability

| Scenario | Success Rate | Daily Profit |
|----------|--------------|--------------|
| Strong miner | 80% | ~0.85 TAO |
| Average miner | 65% | ~0.45 TAO |
| Weak miner | 50% | ~0.05 TAO |
| Break-even | ~45% | 0 TAO |

**Key insight:** Failed challenges still cost subnet fees but earn zero emissions. Success rate is the primary profitability driver.

---
