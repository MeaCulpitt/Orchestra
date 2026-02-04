# ⚙️ Incentive & Mechanism Design: SN-Orchestra

This document outlines the economic and algorithmic framework that governs the **SN-Orchestra** subnet. Our design is optimized for the **Dynamic TAO (dTAO)** era, ensuring that rewards are proportional to the genuine managerial intelligence and economic effort provided by participants.

---

## 1. Emission and Reward Logic
SN-Orchestra operates under the **Yuma Consensus (YC3)** framework, utilizing a market-driven emission schedule tied to the subnet's specific liquidity pool.

* **The Alpha Token ($\alpha$):** All internal rewards are denominated in the subnet's native token. The emission rate is dynamically adjusted based on the TAO-to-Alpha reserve ratio, reflecting the market's valuation of the orchestration service.
* **Reward Split:**
    * **Miners (41%):** Distributed via the **Orchestration Efficiency Score (OES)**.
    * **Validators (41%):** Distributed based on **Dividends** and **V-Trust** (accuracy of ranking).
    * **Subnet Owner (18%):** Directed to the owner's hotkey for protocol maintenance.
* **The OES Formula:** $$OES = (W_{r} \cdot Reasoning) + (W_{f} \cdot Fidelity) + (W_{u} \cdot Utility)$$
  This multi-objective function ensures that miners are not just fast, but logically sound and resource-efficient.

---

## 2. Incentive Alignment
We align the interests of all participants to foster a self-correcting, high-utility ecosystem.

* **Miners (The Project Managers):** Incentivized to minimize internal costs (hiring external expert subnets like **SN62** or **SN64**) while maximizing the quality of the final synthesis. Superior routing directly leads to higher Alpha yields.
* **Validators (The Logic Auditors):** Incentivized to maintain high **Consensus Weight**. By correctly identifying the most efficient miners, validators maximize their own dividends. Validators are also encouraged to provide high-bandwidth API gateways to capture external organic demand.

---

## 3. Adversarial & Low-Quality Discouragement
To maintain the integrity of the "Manager" layer, we implement several defensive layers:

* **Hash-Locked Execution Proofs:** Miners must provide the cryptographic signature from the external subnet's validator for every task they "hired" out. Failure to provide a valid signature results in a zero score for that task.
* **Synthetic Logic Traps:** Validators inject "known-answer" complex tasks into the workstream. If a miner's response deviates from the logically optimal path or hallucinates sub-task results, they face immediate score pruning.
* **Plagiarism Penalties:** The protocol detects and penalizes "weight-copying" or response-duplication between miners to ensure competitive diversity.

---

## 4. Proof of Intelligence & Proof of Effort
SN-Orchestra moves beyond simple compute-sharing to verify higher-order cognitive work.

* **Proof of Intelligence:** To complete an `OrchestraSynapse`, a miner must execute a logical decomposition of a goal into a Directed Acyclic Graph (DAG). This requires high-level reasoning that cannot be faked with static scripts.
* **Proof of Effort:** Because miners must spend TAO or Alpha to "hire" work from other subnets (e.g., Code from **Ridges**), every submission carries an inherent **Economic Cost of Production**. This makes sybil attacks and spam economically non-viable.

---

## 5. High-Level Algorithm
The SN-Orchestra lifecycle follows a five-step loop every block:

1. **Task Assignment:** Validators receive an objective and broadcast it to the miner pool.
2. **Task Decomposition:** Miners use reasoning agents to plan the multi-subnet execution.
3. **External Procurement:** Miners call external subnets (SN62, SN64, etc.) and collect signed response hashes.
4. **Synthesis & Submission:** Miners aggregate the work into a final payload and submit it to the Validator.
5. **Validation & Reward:** Validators audit the "Receipts" (hashes) and the "Synthesis" quality, updating the weight matrix on the Subtensor blockchain.
