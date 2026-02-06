# 🛠️ Miner Design: The Strategic Dispatcher

Miners in the SN-Orchestra subnet act as the "Managerial Intelligence" of Bittensor. Unlike traditional compute miners, Orchestra miners specialize in task decomposition, cross-subnet resource procurement, and the high-fidelity standardization of JSON data structures.

---

## 1. Miner Tasks
The miner's workflow is a multi-stage process that transforms a raw validator request into a verified, structured solution.

### A. Intent Decomposition & Planning
Upon receiving a `OrchestraSynapse`, the miner must first analyze the complexity of the prompt. It utilizes a local reasoning engine (e.g., Llama-3-70B or equivalent) to generate an **Execution DAG** (Directed Acyclic Graph), identifying which external subnets are required for each sub-task.

### B. Expert Procurement (Cross-Subnet Routing)
The miner acts as an "Agentic Buyer," selecting the best UIDs from specialized subnets.
* **Code:** Interfaces with SN62 (Ridges).
* **Data Retrieval:** Interfaces with SN13 (Data Universe) or SN5 (OpenKaito).
* **Search:** Interfaces with SN22 (Smart Search).

### C. JSON Standardization Layer (The Normalization Engine)
One of the most critical tasks is the **Standardization Layer**. When a miner retrieves data from multiple subnets, that data is often "noisy" and disparate in format. The miner must:
* **Normalize:** Map varying keys (e.g., `user_id` vs `uid`) to a unified schema.
* **Validate:** Ensure the JSON is structurally sound and typed according to the validator's requirements.
* **Enrich:** Inject metadata such as the source subnet ID and a "Trust Score" for each data point.

---

## 2. Expected Input → Output Format
Miners communicate using the `OrchestraSynapse`, ensuring a strict data contract for every interaction.

### Input (From Validator)
* **`objective` (str):** The high-level task (e.g., "Retrieve 2026 tech trends and format as a React-ready JSON").
* **`target_schema` (dict):** The specific JSON structure the validator expects for the final data.
* **`max_latency` (int):** The block-time deadline for submission.

### Output (To Validator)
* **`final_completion` (str):** The human-readable synthesis of the work.
* **`standardized_data` (json):** The normalized JSON payload, structured exactly to the `target_schema`.
* **`task_pipeline` (list):** A verifiable log of every external subnet call, containing:
    * `subnet_id`: The ID of the expert subnet called.
    * `external_uid`: The UID of the expert miner used.
    * `proof_hash`: The cryptographic hash of the transaction proof.

---

## 3. Performance Dimensions
Miners are ranked relative to their peers across four key metrics. To maintain a top-tier UID, miners must balance these dimensions:

| Dimension | Metric | Description |
| :--- | :--- | :--- |
| **Logic Fidelity** | **Reasoning Score** | Measured by the Judge LLM’s assessment of the decomposition path. |
| **Data Accuracy** | **Schema Matching** | Percentage of fields in `standardized_data` that match the `target_schema` perfectly. |
| **Fidelity** | **Hash Verification** | Verification of signed receipts from external subnets; invalid hashes result in a zero score. |
| **Velocity** | **Block Latency** | Time taken to synthesize and return results. Faster miners receive a "Speed Multiplier" in the OES. |

---

## 🏗️ Hardware Requirements (Estimated 2026)
* **GPU:** 1x RTX 4090 or A100 (Minimum 24GB VRAM for local reasoning and JSON parsing).
* **CPU:** 16+ Cores (High concurrency for managing multiple asynchronous subnet calls).
* **Bandwidth:** 1Gbps+ (Critical for fetching large JSON payloads from data subnets).
