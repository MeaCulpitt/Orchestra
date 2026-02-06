# 🛠️ Miner Design: The Strategic Lead (General Contractor)

Miners in the Orchestra subnet do not provide raw compute; they provide **Managerial Compute**. A successful Miner acts as the General Contractor of the Bittensor ecosystem, specializing in intent-to-execution mapping and cross-subnet resource procurement.

---

## 1. Core Responsibilities: The Lifecycle of a Project
The Miner's operations are divided into three distinct phases of "Executive Work":

### A. Phase 1: Intent Decomposition & Pipeline Planning
Upon receiving an `OrchestraSynapse`, the Miner utilizes a local high-reasoning engine (e.g., Llama-3.1-70B or customized Mistral Large) to:
* Identify the **Prerequisite Graph**: What information is needed first?
* Generate the **Execution DAG**: A step-by-step roadmap of which specialized subnets (Experts) must be called and in what order.
* **Cost-Benefit Analysis**: Determine the optimal Alpha/TAO spend vs. the expected reward from the Validator.

### B. Phase 2: Expert Procurement & Management
The Miner orchestrates the work across the metagraph:
* **UID Discovery**: Querying specialized subnets (SN62 for code, SN13 for data, SN22 for search) to find the highest-performing UIDs.
* **Asynchronous Execution**: Managing multiple simultaneous calls to prevent latency penalties.
* **Quality Control (QC)**: If an expert returns a hallucination or an error, the Miner must detect it and "re-hire" a different UID to ensure the final synthesis is accurate.

### C. Phase 3: The JSON Standardization Layer
This is the "Final Inspection" before delivery. The Miner must:
* **Normalize**: Align disparate JSON keys (e.g., `user_id` vs `uid`) to the Validator's `target_schema`.
* **Type Enforcement**: Use Pydantic models to ensure floats, strings, and lists are correctly typed.
* **Provenance Tagging**: Inject metadata identifying which expert subnets provided each piece of data.

---

## 2. Expected Input → Output Format
Miners must adhere to the strict `OrchestraSynapse` contract:

* **Input (Validator):**
    * `objective` (str): The complex task (e.g., "Analyze SN13 tech trends and generate a Python viz").
    * `target_schema` (json): The required structure for the final standardized data.
* **Output (Miner):**
    * `task_pipeline` (list): A step-by-step log of every subnet called, including UID and hash-locked proof.
    * `standardized_data` (json): The normalized, type-safe payload.
    * `final_synthesis` (str): The human-readable summary of the completed project.

---

## 3. Hardware Requirements (Estimated 2026)
* **GPU:** 1x RTX 4090 or A100 (Required for local LLM-based decomposition and synthesis).
* **RAM:** 64GB+ (To handle high-concurrency async operations).
* **Network:** 1Gbps+ (Critical for high-volume JSON ingestion from multiple subnets).
