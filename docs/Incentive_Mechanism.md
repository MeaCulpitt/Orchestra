# 🎻 Orchestra Incentive & Mechanism Design

Orchestra utilizes a dual-objective incentive model designed to reward both **Strategic Coordination** and **Data Integrity**. By splitting the incentive landscape, the network ensures that miners are rewarded for solving complex problems while simultaneously maintaining the ecosystem's most accurate directory of intelligence.

---

## 1. Emission and Reward Logic
Orchestra employs a **70/30 Reward Split** to balance its dual functions:

* **70% - Coordination & Synthesis (The Lead Architect):** This majority share is allocated to the "Work" performed by the miner. It measures the miner's ability to decompose a complex objective, procure the correct expert subnets (e.g., SN19 for data, SN103 for reasoning), and synthesize the results into a high-value package.
* **30% - Schema Accuracy (The Subnet Ledger):** This share rewards the "Record." It measures the fidelity of the miner’s Subnet Ledger. Miners must provide Pydantic-validated schemas that accurately reflect the current output signatures of the subnets they are managing.



---

## 2. Incentive Alignment for Miners and Validators
The mechanism aligns all participants toward a single goal: **Production-Ready Intelligence.**

* **Miners:** To maximize rewards, miners cannot simply "proxy" data. They must optimize their routing logic to find the highest-performing subnets for a given task. Because 30% of their reward depends on the Ledger, they are incentivized to contribute to the network’s collective intelligence by keeping their subnet maps updated.
* **Validators:** Validators act as "Executive Auditors." They are incentivized to provide accurate scoring because their own vTrust depends on reaching a consensus with other validators regarding the quality of a miner’s synthesis and the accuracy of their schema data.

---

## 3. Mechanisms to Discourage Low-Quality or Adversarial Behavior
Orchestra utilizes a multi-layered "Anti-Fragility" protocol:

* **Schema Traps:** Validators occasionally issue "Trap Requests" where they already know the target schema for a specific subnet. If a miner provides an outdated or hallucinated Ledger entry, their accuracy score is slashed.
* **Synthesis Verification:** Validators use high-reasoning LLMs to compare the miner’s final output against the raw data from the experts used in the pipeline. If a miner "fakes" a synthesis or fails to include the work of the subnets they claimed to hire, the submission is discarded.
* **Redundancy Checks:** For high-value tasks, validators may compare the outputs of multiple miners. If one miner consistently provides outliers or lower-quality synthesis than the cohort, their weights are reduced via the consensus mechanism.

---

## 4. Proof of Intelligence and Proof of Effort
Orchestra qualifies as a genuine **Proof of Intelligence** by requiring high-level cognitive work:

* **Strategic Decomposition:** A miner must "understand" a request well enough to know that a coding task requires a different pipeline than a legal research task. This is a non-trivial reasoning step that cannot be solved by brute force.
* **Proof of Effort (The Audit Trail):** Every submission must include a "Task Pipeline" log. This serves as a Proof of Effort, showing exactly which subnets were called and the hash proofs of those interactions. The network does not reward "answers"; it rewards the **managed process** of reaching those answers.



---

## 5. High-Level Algorithm
The Orchestra execution cycle follows a deterministic five-step process:

1.  **Task Assignment:** A Validator issues an `OrchestraSynapse` containing a high-level **Objective** and a **Target JSON Schema**.
2.  **Strategic Execution:** The Miner decomposes the objective, queries the Subnet Ledger to identify the best experts, and executes the multi-subnet pipeline.
3.  **Standardized Submission:** The Miner maps the synthesized results to the **Target Schema** and submits the final package, including the **Task Pipeline** log.
4.  **Multi-Dimensional Scoring:**
    * **$S_{coordination}$:** Score based on the relevance and quality of the synthesized output.
    * **$S_{ledger}$:** Score based on the accuracy of the Pydantic models used for the expert subnets.
5.  **Reward Allocation:** The final weight $W$ is calculated as:
    $$W = (0.7 \times S_{coordination}) + (0.3 \times S_{ledger})$$
    Weights are then committed to the subchain for $TAO$ emission.
