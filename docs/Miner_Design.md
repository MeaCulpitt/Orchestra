# 🛠️ Miner Design: The Strategic Dispatcher

Miners in the SN-Orchestra subnet act as **Strategic Dispatchers** rather than raw compute providers. Their core value is "Orchestration Intelligence"—the ability to receive a complex human objective and execute a high-fidelity solution by coordinating specialized experts across the Bittensor network.

---

## 1. Miner Tasks
The miner's operational lifecycle is divided into three distinct cognitive layers:

### A. Intent Decomposition (The Planner)
Upon receiving a `OrchestraSynapse`, the miner must first parse the high-level objective into a **Directed Acyclic Graph (DAG)** of sub-tasks. 
* **Example:** For the prompt *"Analyze current AI trends and generate a summary report with code examples,"* the miner identifies three distinct phases: **Retrieval** (SN13), **Reasoning/Synthesis** (SN1), and **Code Generation** (SN62).

### B. Expert Selection & Procurement (The Negotiator)
The miner acts as a "Meta-Client" (Dendrite). Using real-time metagraph data, the miner identifies the highest-performing UIDs in external subnets to fulfill each node of the DAG. 
* **Protocol:** The miner sends specialized Synapses to these external axons and manages the asynchronous response flow.
* **Economic Effort:** Miners must manage their own Alpha/TAO liquidity to pay for these external services, ensuring every submission carries a verifiable "Cost of Production."

### C. Synthesis & Delivery (The Architect)
Once the sub-results are gathered, the miner integrates them into a single, cohesive response. This requires an internal "Synthesis LLM" to ensure the final output is not just a collection of parts, but a polished, human-readable solution.

---

## 2. Expected Input → Output Format
The `OrchestraSynapse` serves as the standardized communication contract between the Validator and the Miner.

### Input (From Validator)
| Field | Type | Description |
| :--- | :--- | :--- |
| `objective` | `str` | The high-level multi-step task (e.g., "Build a React site based on X"). |
| `context` | `dict` | Metadata: preferred subnets, latency caps, and output formatting. |
| `timeout` | `int` | The maximum time allowed for the full orchestration loop. |

### Output (From Miner)
| Field | Type | Description |
| :--- | :--- | :--- |
| `final_completion` | `str` | The final synthesized solution provided to the end user. |
| `task_pipeline` | `list` | A JSON log of external calls: `[{"subnet": 62, "hash": "0x...", "status": "success"}]`. |
| `reasoning_path` | `str` | A brief technical justification for the chosen orchestration strategy. |

---

## 3. Performance Dimensions
Miners are ranked and rewarded based on four primary vectors of the **Orchestration Efficiency Score (OES)**:

* **Logical Fidelity ($W_{f}$):** Does the `task_pipeline` logically map to the `objective`? Validators penalize "hallucinated" steps or skipped dependencies.
* **Expertise Selection ($W_{e}$):** Miners are rewarded for selecting external UIDs with high ranks in their respective subnets, ensuring "Best-in-Class" results.
* **Synthesis Quality ($W_{q}$):** The coherence, accuracy, and formatting of the `final_completion`.
* **Latency ($W_{s}$):** The efficiency of the "Routing Layer." In an agentic economy, a slow manager is a failed manager.

---

## 4. Hardware Requirements
Because the "work" is delegated, the hardware focus shifts from high-VRAM GPUs to high-concurrency CPU and networking performance.

* **CPU:** 8+ vCPUs (Optimized for asynchronous I/O and routing).
* **RAM:** 16GB+ (To maintain local task buffers and routing tables).
* **Storage:** 100GB NVMe (For logging and metagraph synchronization).
* **Network:** 1Gbps+ symmetric (Crucial for multi-subnet "round-trip" orchestration).
