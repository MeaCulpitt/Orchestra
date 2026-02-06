# ⚙️ Incentive & Mechanism Design: Orchestra

The Orchestra incentive mechanism is engineered to reward **Executive Intelligence**. In the Bittensor ecosystem of 2026, raw compute is a commodity; the ability to manage, verify, and standardize that compute into a finished product is the alpha.

---

## 1. Emission and Reward Logic
SN-Orchestra operates on a dual-incentive structure within the Yuma Consensus framework. Emissions are distributed based on a Miner’s ability to act as a high-fidelity "General Contractor."

* **Validator Rewards (18%):** Distributed based on V-Trust and the accuracy of their audits.
* **Miner Rewards (82%):** Distributed based on the **Orchestration Efficiency Score (OES)**.

To ensure long-term sustainability, 30% of the Miner emission pool is specifically earmarked for the **JSON Standardization Layer (Mechanism 1)**, while 70% rewards the **Strategic Routing & Pipeline Management (Mechanism 0)**.

---

## 2. The Orchestration Efficiency Score (OES)
The OES is a multi-variate formula that mathematically defines the "Quality of Management."

$$OES = (W_{r} \cdot R) + (W_{p} \cdot P) + (W_{d} \cdot D) + (W_{v} \cdot V)$$

| Component | Variable | Definition |
| :--- | :--- | :--- |
| **Reasoning** | $R$ | The logical validity of the Task Decomposition DAG. |
| **Procurement** | $P$ | Verifiable proof (hashes) of expert hiring across the metagraph. |
| **Data Integrity** | $D$ | Adherence to the strict JSON Standardization Layer requirements. |
| **Velocity** | $V$ | A multiplier for sub-second coordination and synthesis. |

---

## 3. Managerial Alignment: Proof of Effort & Intelligence
Orchestra qualifies as a genuine **Proof of Intelligence (PoI)** system because it requires miners to solve the "Coordination Problem."

1. **Proof of Effort (The Procurement Gate):** Miners cannot spoof results. To receive a score above zero, a miner must provide cryptographic transaction hashes from external subnets. This ensures the miner has "skin in the game" by spending resources to fulfill the user's request.
2. **Proof of Intelligence (The Reasoning Gate):** Validators inject **Logic Traps**—tasks where a naive routing path will lead to an incorrect synthesis. Miners must use local high-reasoning models to navigate these traps, proving they are actively "managing" the pipeline rather than blindly forwarding packets.

---

## 4. High-Level Algorithm: The Execution Lifecycle
The following 7-step sequence describes the lifecycle of a single orchestration event:

1. **Intent Broadcast:** The Validator broadcasts a complex objective and a `target_schema` to the miner pool.
2. **Decomposition:** The Miner generates a **Task DAG**, identifying the specific subnets (Experts) required to fulfill the request.
3. **Execution & Routing:** The Miner programmatically "hires" the identified Experts, managing the asynchronous timing of their responses.
4. **The Managerial Loop (Verification):** The Miner audits the Expert outputs. If an Expert provides a low-quality or malformed response, the Miner is incentivized to re-route to a different UID to protect their own OES.
5. **JSON Standardization:** The Miner passes the "dirty" Expert data through the **Standardization Layer**, mapping it to the requested schema and enriching it with provenance metadata.
6. **Submission:** The Miner returns the `standardized_data` and the `task_pipeline` (with execution hashes) to the Validator.
7. **Audit & Scoring:** The Validator verifies the hashes, runs a Pydantic check on the JSON, and utilizes a "Judge LLM" to grade the logic of the initial decomposition. Weights are then set on-chain.

---

## 5. Adversarial Defenses
* **Collusion Penalties:** Validators utilize semantic similarity checks to identify miners who are sharing the same execution paths or standardized outputs.
* **Hash Blacklisting:** Re-using a transaction hash from a previous epoch or a different miner results in an immediate and permanent "black-rooming" of the UID.
