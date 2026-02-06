# 🎻 Orchestra Miner Design: The Lead Architect

In the Orchestra network, miners do not perform raw compute. They operate as **Lead Architects**—strategic managers who coordinate a global supply chain of decentralized intelligence to deliver finished project packages.

---

## 1. Primary Tasks: The Project Lifecycle
A miner’s primary responsibility is the successful execution of complex, multi-subnet objectives. This work is divided into three critical management phases:

* **Task Decomposition:** Upon receiving a high-level objective, the miner must utilize a high-reasoning model to break the goal into a logical sequence of sub-tasks.
* **Expert Procurement:** Using their internal Subnet Ledger, the miner identifies and programmatically "hires" the best-performing expert subnets to fulfill each stage of the roadmap.
* **Synthesis & Delivery:** The miner aggregates the disparate outputs from these experts, performs a final quality audit, and packages the result into a single, high-value solution for the user.

---

## 2. Secondary Task: Ledger Maintenance (The Manager's Map)
To lead effectively, an Architect must know their workforce. **Ledger Maintenance** is the essential background function that powers the management engine.

* **Real-Time Polling:** Miners must continuously poll the metagraph to detect changes in subnet capabilities, latency, and reliability.
* **Standardization (The Byproduct):** Miners maintain Pydantic-validated schemas for every subnet they manage. This ensures that when the Lead Architect delivers a project, the data is structured, type-safe, and deterministic—eliminating the "fragmentation tax" for the end user.


---

## 3. Expected Input → Output Format
Miners communicate via the `OrchestraSynapse`, adhering to a strict professional contract:

### Expected Input (From Validator)
* **`objective` (String):** A complex, multi-dimensional goal.
* **`target_schema` (JSON/Dict):** The required structure for the final output.

### Expected Output (To Validator)
* **`task_pipeline` (List[Dict]):** A detailed log of the experts hired, including cryptographic hash-proofs of their responses.
* **`standardized_data` (JSON/Dict):** The final project results, formatted strictly to the target schema.
* **`final_synthesis` (String):** A human-readable executive summary of the project’s outcome.

---

## 4. Performance Dimensions
Miner weights are calculated based on their efficiency as managers and the accuracy of their internal records:

| Dimension | Weight | Metric |
| :--- | :--- | :--- |
| **Management Quality** | **70%** | The depth of decomposition and the utility of the final synthesis. |
| **Record Integrity** | **30%** | The accuracy of the Subnet Ledger data against the live state of the experts. |
| **Speed (Latency)** | **Multiplier** | Efficient miners with high-speed async pipelines receive a reward multiplier. |

---

## 5. Technical Requirements
* **Asynchronous Orchestration:** Miners must handle concurrent calls to multiple external subnets without blocking.
* **Pydantic Registry:** Miners must maintain a local database of validated schemas for all supported subnets.
* **Verification Logic:** Miners should perform internal audits of expert outputs before synthesis to ensure high-fidelity delivery to the Validator.
