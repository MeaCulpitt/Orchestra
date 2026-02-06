The SN-Orchestra incentive mechanism is designed to reward "Managerial Alpha"—the ability to efficiently decompose, route, and synthesize complex tasks and data. By implementing a multi-layered verification protocol, the subnet ensures that emissions flow toward miners who contribute genuine orchestration value.

---

## 1. Emission and Reward Logic
SN-Orchestra follows the **Yuma Consensus** model for reward distribution. Every 360 blocks (one tempo), the subtensor blockchain calculates emissions based on the weight matrices submitted by validators.

* **Validator Emissions:** 18% of the subnet's total emission is distributed to validators based on their **V-Trust** (consensus with other validators).
* **Miner Emissions:** 82% of the emission flows to miners based on their **Orchestration Efficiency Score (OES)**.
* **Recycling:** In 2026, a 2% "Development Fee" is recycled into the subnet's **Alpha Liquidity Pool** to stabilize the token price and incentivize long-term participation.

---

## 2. Incentive Alignment for Miners and Validators
We utilize a "Dual-Incentive" structure to align the interests of all participants with the quality of the network.

### For Miners: The Efficiency Flywheel
Miners are incentivized to optimize for **Cost-to-Quality ratios**. Because miners must pay for services on external subnets (e.g., SN62 for code), they are naturally incentivized to select the highest-performing yet most cost-effective "Experts." A miner who overspends on sub-tasks reduces their own profit margin, while a miner who uses "cheap/bad" experts fails the validator's quality audit.

### For Validators: The Reputation Bond
Validators earn dividends proportional to their stake and their consensus score. If a validator diverges from the group by rewarding "junk" miners, their V-Trust drops, directly reducing their TAO and Alpha earnings. This forces validators to constantly refine their judging LLMs and logic traps.

---

## 3. Mechanisms to Discourage Adversarial Behavior
To protect the subnet from "collusion cabals" and "lazy mining," we implement three specific defense layers:

* **Hash-Locked Execution Proofs:** Miners must provide the cryptographic transaction hash for every sub-task performed on an external subnet. If the hash is missing or belongs to a different UID, the miner is blacklisted.
* **Logic Trap Injection:** Validators periodically send "Golden Tasks" (tasks with known optimal decomposition paths). Miners who fail these hidden tests are severely penalized in the ranking matrix.
* **JSON Schema Enforcement:** For data-centric tasks, miners must return information in a strict, pre-defined JSON format. Failure to normalize data from disparate subnets results in a "Format Penalty," ensuring the subnet remains useful for downstream LLMs.

---

## 4. Proof of Effort & Intelligence
SN-Orchestra qualifies as a **"Proof of Effort"** (PoE) and **"Proof of Intelligence"** (PoI) system because:

1. **Proof of Effort:** To provide a valid `task_pipeline`, a miner *must* have spent Alpha/TAO on other subnets. This creates a tangible economic "Work Proof" that cannot be spoofed without actual network participation.
2. **Proof of Intelligence:** Decomposition is a high-reasoning task. A miner cannot simply "copy-paste" from an API; they must dynamically map a human intent to a machine-readable DAG and transform raw JSON into structured knowledge.

---

## 5. High-Level Algorithm
The following sequence describes a single orchestration epoch, incorporating both task execution and data standardization:

1. **Task Assignment:** The Validator generates a multi-objective prompt or a data-retrieval request and broadcasts the `OrchestraSynapse` to the top 256 miners.
2. **Decomposition & Mapping:** The Miner decomposes the task into sub-steps and maps the required data outputs to a **Unified JSON Schema**.
3. **Execution (Routing):** The Miner queries external specialized subnets, collecting both the raw responses and the signed response hashes.
4. **Standardization (The Data Layer):** The Miner transforms disparate JSON information from external subnets into the standardized format requested by the validator, enriching it with contextual metadata.
5. **Submission:** The Miner populates the `task_pipeline`, `final_completion`, and `standardized_data` fields and returns the Synapse.
6. **Validation:** The Validator verifies the external hashes, audits the reasoning path using a "Judge LLM," and checks the integrity of the JSON structure against the target schema.
7. **Scoring:** The Validator calculates the OES: 
   $$OES = (W_{r} \cdot Reasoning) + (W_{f} \cdot Fidelity) + (W_{u} \cdot Utility) + (W_{d} \cdot Data\_Integrity)$$
8. **Reward Allocation:** Scores are converted into a weight vector $W$ and committed to the blockchain for the next emission cycle.
