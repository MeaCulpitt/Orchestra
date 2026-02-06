# ⚖️ Validator Design: The Logic & Data Auditor

Validators on SN-Orchestra serve as the "Source of Truth" for orchestration quality and data integrity. They are responsible for auditing miner performance, verifying cross-subnet execution proofs, and enforcing the JSON Standardization Layer to ensure the network delivers high-utility, structured intelligence.

---

## 1. Scoring and Evaluation Methodology
The scoring process on SN-Orchestra is a multi-dimensional audit that evaluates both the "Managerial Logic" and the "Data Fidelity" of the miner's response.

### A. The Orchestration Efficiency Score (OES)
Validators calculate a weighted score based on four primary pillars:
$$OES = (W_{r} \cdot Reasoning) + (W_{f} \cdot Fidelity) + (W_{u} \cdot Utility) + (W_{d} \cdot Data\_Integrity)$$

* **Reasoning ($W_{r}$):** Evaluated via a high-tier Consensus Judge LLM (e.g., SN1 Apex) to ensure the decomposition of the task was logically sound.
* **Fidelity ($W_{f}$):** Structural verification of **Hash-Locked Execution Proofs**. Validators verify the cryptographic signatures from external subnets to confirm the miner actually "hired" the claimed experts.
* **Utility ($W_{u}$):** A semantic grade of the final synthesized answer compared against a "Golden Reference" for synthetic tasks.
* **Data Integrity ($W_{d}$):** Verification of the **JSON Standardization Layer**. Validators check the miner's `standardized_data` against a target schema (Pydantic-based validation) to ensure it is machine-readable and error-free.

### B. Logic & Schema Traps
Validators periodically inject "Trap Tasks" which include:
* **Logic Traps:** Challenges with a hidden dependency that a "lazy" miner will likely skip.
* **Schema Traps:** Requests with complex or non-standard JSON requirements. Miners who fail to normalize this data to the exact schema are heavily penalized.

---

## 2. Evaluation Cadence
To maintain a high-performance metagraph in the 2026 dTAO environment, validation occurs on two distinct temporal tracks:

* **Synthetic Challenges (Leaderboard Track):** Every **20 blocks** (approx. 4 minutes), the validator sends a hidden synthetic probe to all miners. This ensures the metagraph is constantly re-ranked based on current latency and accuracy.
* **Organic Auditing (Service Track):** For organic API traffic, validators perform "Spot Checks." They intercept a sample of real-world responses to ensure miners maintain the same quality for users as they do for synthetic probes.
* **Weight Commitment:** Every **360 blocks (one tempo)**, validators aggregate these moving averages and commit the weight matrix to the Subtensor blockchain, triggering the distribution of Alpha and TAO emissions.

---

## 3. Validator Incentive Alignment (dTAO Model)
Under the **Dynamic TAO** framework, validators are economically bonded to the subnet’s accuracy and reputation.

* **V-Trust (Consensus Alignment):** A validator's rewards are tied to their **V-Trust** score. If a validator’s rankings diverge from the stake-weighted median of the network (e.g., by rewarding a "collusion cabal"), their emissions are slashed.
* **Alpha Staking Dividends:** Validators earn dividends in the subnet’s native **Alpha token ($\alpha$)**. By effectively filtering out low-quality miners and promoting high-utility data orchestration, validators increase the subnet's overall market value, directly benefiting their own staked position.
* **The Reputation Market:** In 2026, high-performing validators attract more delegated stake. By maintaining a superior "Standardization Layer," validators prove to the community that the subnet provides real-world utility, securing their position in the top 64 validator slots.

---

## 4. Proof of Intelligence: Data Orchestration
By enforcing the **JSON Standardization Layer**, validators provide a verifiable "Proof of Intelligence." A miner cannot simply relay raw data; they must demonstrate the cognitive effort of mapping, cleaning, and structuring disparate information into a unified format. This transforms the subnet from a simple router into a high-value **Knowledge Factory**.
