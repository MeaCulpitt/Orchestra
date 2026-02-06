# 🎻 Orchestra Miner Design

In the Orchestra subnet, Miners operate as **Lead Architects**. Unlike traditional subnets where miners perform a singular compute task, Orchestra Miners are evaluated on their ability to manage complex workflows and maintain a high-fidelity record of the Bittensor ecosystem.

---

## 1. Miner Tasks
A Miner’s operational cycle is divided into two continuous workstreams:

### A. Managed Pipeline Execution (The Architect)
When a request is received, the Miner must:
* **Deconstruct the Objective:** Break down a high-level user prompt into a logical sequence of sub-tasks.
* **Expert Procurement:** Query the internal Subnet Ledger to identify which subnets (e.g., SN5, SN19, SN22) possess the specific expertise required for the current roadmap.
* **Inter-Subnet Routing:** Call the selected subnets, handle their specific authentication/synapse requirements, and collect raw intelligence.
* **Synthesis & Mapping:** Aggregate the disparate data points and map them into the requested final schema.

### B. Ledger Maintenance (The Bookkeeper)
Independent of specific tasks, Miners must:
* **Metagraph Polling:** Periodically "ping" and sample outputs from across the Bittensor network to detect changes in subnet behavior or data structures.
* **Schema Validation:** Update local Pydantic models to ensure the Miner’s internal map of the ecosystem matches the live reality of other subnets.
* **Optimization:** Track the performance (latency and quality) of other subnets to ensure future routing decisions are data-driven.



---

## 2. Expected Input → Output Format
Miners communicate via the `OrchestraSynapse`, which enforces a strict contract between the Validator's request and the Miner's delivery.

### Expected Input (From Validator)
* **`objective` (String):** A complex, multi-stage goal (e.g., "Research the latest decentralized AI trends and output a SWOT analysis in JSON").
* **`target_schema` (JSON/Dict):** A Pydantic-compatible schema defining exactly how the Miner must structure the final response.

### Expected Output (To Validator)
* **`task_pipeline` (List[Dict]):** A transparent log of the expert subnets called, including the specific Synapse types used and the cryptographic hashes of the responses received.
* **`standardized_data` (JSON/Dict):** The final synthesized result, strictly adhering to the `target_schema`.
* **`final_synthesis` (String):** A human-readable executive summary of the project’s completion.

---

## 3. Performance Dimensions
Miner performance is graded across three primary vectors, which directly influence the weight ($W$) assigned by Validators.

### A. Quality of Synthesis (Weight: 40%)
The synthesis is evaluated on its comprehensiveness. Validators check if the Miner successfully integrated all necessary components of the objective. A high-quality response isn't just a "summary"; it is an enriched data package that provides more value than the sum of its raw parts.

### B. Ledger Accuracy (Weight: 30%)
The Miner’s ability to correctly identify and use the right subnets is critical. If a Miner routes a coding task to a search subnet, or provides a data structure that breaks the `target_schema`, the Accuracy score is penalized. This ensures the **Subnet Ledger** remains a "Standard of Truth."



### C. Speed & Efficiency (Weight: 30%)
In a production environment, latency is a product killer. Miners are timed on their "Time to Synthesis." This includes the time taken to plan, call external subnets, and format the data. To score high here, Miners must implement efficient asynchronous calling and maintain a "hot" local cache of the Subnet Ledger.

---

## 4. Operational Requirements
* **Asynchronous Networking:** Miners must be capable of handling multiple concurrent requests and outgoing subnet calls without blocking.
* **Pydantic Proficiency:** The ability to dynamically map unstructured data into strict schemas is the Miner's core technical advantage.
* **Metagraph Awareness:** Miners must maintain an active `bt.metagraph` object to stay synchronized with the evolving state of the network.
