# 🎻 Orchestra Incentive & Mechanism Design

Orchestra rewards **Proof of Management**. The incentive structure is designed to attract miners who can effectively lead complex multi-subnet projects while maintaining a perfect record of the network's capabilities—an essential byproduct of the management process.

---

## 1. Emission and Reward Logic (70/30)

To ensure the subnet delivers professional-grade results, we employ a dual-objective reward split:

### 🏆 70% - Strategic Coordination (The Lead Architect)
The majority of the reward is allocated to the miner's ability to act as a **General Contractor**. This measures the "Proof of Effort" in:
* **Task Decomposition:** The cognitive effort of breaking a complex goal into a specialized roadmap.
* **Expert Procurement:** The strategic choice of which expert subnets (e.g., SN1, SN22, SN103) to hire for the task.
* **Synthesis:** The ability to merge disparate results into a high-value final solution.

### 📋 30% - Ledger Accuracy (The Standard of Record)
This rewards the essential maintenance work required to support the management engine. It measures the fidelity of the miner’s **Subnet Ledger**:
* **Schema Integrity:** Miners are rewarded for providing Pydantic-validated data structures that accurately reflect the current output signatures of the experts they are managing.
* **Fidelity:** This ensures that the Lead Architect's delivered package is deterministic and production-ready for enterprise clients.


---

## 2. The Incentive Alignment
* **Miners:** To maximize revenue, miners must optimize their "supply chain." They are incentivized to identify the highest-performing expert subnets and maintain an accurate Ledger, as a broken map leads to failed management and zero rewards.
* **Validators:** Validators act as **Executive Auditors**. They verify the miner’s "Work Logs" to ensure experts were actually called and use high-reasoning models to score the quality of the final synthesis.

---

## 3. The Validation Algorithm (Proof of Management)
1. **Request:** A Validator issues an `OrchestraSynapse` containing a complex project objective.
2. **Orchestration:** The Miner decomposes the task and queries 2+ expert subnets based on their internal Ledger.
3. **Delivery:** The Miner submits the final package, including a standardized JSON record of the experts' work.
4. **Scoring:**
   * **$S_{coordination}$ (70%):** Scored on the logical depth of the decomposition and the utility of the synthesized answer.
   * **$S_{ledger}$ (30%):** Scored on the accuracy of the data schemas against the live state of the experts used.
5. **Final Reward:** $W = (0.7 \times S_{coordination}) + (0.3 \times S_{ledger})$.

---

## 4. Adversarial Resistance & Quality Control
* **Hash Auditing:** Miners must provide cryptographic proofs of their interactions with expert subnets. Validators cross-reference these hashes to prevent miners from "faking" the management process.
* **Schema Traps:** Validators occasionally issue requests for subnets with known, volatile schemas. If a miner's Ledger entry is outdated or incorrect, they lose the accuracy portion of their reward, incentivizing continuous record-keeping.
