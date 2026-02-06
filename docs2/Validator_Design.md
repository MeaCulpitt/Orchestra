# ⚖️ Validator Design: The Executive Auditor

The SN-Orchestra Validator ensures the integrity of the "Managerial Layer." It does not just grade the final answer; it audits the Miner's decision-making process, ensuring they are acting as efficient project managers rather than simple pass-through proxies.

---

## 1. Scoring & Evaluation Methodology
The Validator calculates the **Orchestration Efficiency Score (OES)** through a rigorous four-part audit:

### A. The Logic Audit (The "Brain" Check)
The Validator uses a high-tier "Judge LLM" (e.g., GPT-4o or SN1 Apex) to evaluate the Miner's `task_pipeline`.
* **Score Factor:** Was the decomposition logical? Did the miner use the correct subnets?
* **Trap Detection:** If the Miner missed a "Logic Trap" injected by the Validator, the Reasoning score is decimated.

### B. The Procurement Audit (The "Work" Check)
The Validator verifies the cryptographic **Hash-Locked Execution Proofs** provided in the `task_pipeline`.
* **Validation:** Every expert call must correspond to a verifiable transaction on the respective subnet's blockchain.
* **Anti-Cheat:** Miners attempting to "simulate" expert data without actually hiring experts are immediately blacklisted.

### C. The JSON Integrity Audit (The "Format" Check)
The Validator runs the Miner's `standardized_data` through a strict Pydantic validation suite.
* **Success:** The JSON perfectly matches the `target_schema`.
* **Failure:** Any type mismatch (e.g., string instead of float) or missing field results in a zero-score for the Standardization component.

---

## 2. Evaluation Cadence & Strategy
Validators maintain high-fidelity rankings through two distinct temporal tracks:

* **Synthetic Probing (Every 20 Blocks):** Rapid-fire challenges designed to test specific edge cases, logic traps, and complex schema requirements. This prevents "Rank Stagnation."
* **Organic Traffic (Real-time):** When a user sends a real request through the Orchestra API, the Validator monitors the fulfillment to ensure production-grade reliability.
* **Weight Setting (Every 360 Blocks):** Aggregated scores are converted into weights and committed to the Subtensor, determining Alpha ($\alpha$) and TAO rewards.

---

## 3. Validator Incentive Alignment
Under the **Dynamic TAO (dTAO)** model, Validators are economically incentivized to protect the subnet's reputation.
* **V-Trust:** Validators who reward low-quality or adversarial miners will see their V-Trust drop, reducing their own emission yields.
* **Value Accrual:** By strictly enforcing the **JSON Standardization Layer**, Validators ensure Orchestra becomes the "Gold Standard" for enterprise RAG, increasing the value of the subnet's native Alpha token.
