# ⚖️ Validator Design: The Logic Auditor

Validators on SN-Orchestra are the "Source of Truth" for orchestration quality. They are responsible for auditing miner performance, verifying cross-subnet execution proofs, and ensuring the network fulfills complex user intents with high fidelity.

---

## 1. Scoring and Evaluation Methodology
Validators utilize a multi-layered verification stack to ensure miners are providing genuine "Managerial Intelligence" rather than spoofing results.

### A. The OES Scoring Formula
Miner performance is quantified via the **Orchestration Efficiency Score (OES)**, a weighted multi-objective optimization function:
$$OES = (W_{r} \cdot Reasoning) + (W_{f} \cdot Fidelity) + (W_{u} \cdot Utility)$$

* **Reasoning ($W_{r}$):** Measures the logical validity of the miner's decomposition (the DAG).
* **Fidelity ($W_{f}$):** Verified via **Hash-Locked Execution Proofs**. Validators check the cryptographic signatures from external subnets (e.g., SN62) to confirm the work was actually performed.
* **Utility ($W_{u}$):** A semantic grade of the final synthesized output compared against a "Consensus Judge" (typically a high-reasoning model like **SN1 Apex**).

### B. Logic Trap Injection
Validators maintain a "Golden Dataset" of complex tasks with known optimal paths. By injecting these "Logic Traps" into the miner workstream, validators can instantly identify miners who attempt to shortcut the decomposition process or hallucinate sub-task outputs.

---

## 2. Evaluation Cadence
The validator operates on two distinct temporal tracks to ensure a live and responsive metagraph:

* **Synthetic Challenges (Warm-Up):** Occurs every **20 blocks** (approx. 4 minutes). This provides a baseline ranking for all 256 UIDs, even in the absence of organic traffic.
* **Organic Auditing (Real-Time):** Organic requests from API gateways are audited as they pass through. Validators intercept a subset of these responses for a "Spot Audit" to ensure consistency between synthetic and real-world performance.
* **Weight Commitment:** Every **360 blocks (one tempo)**, the validator calculates the moving average of all miner scores and commits these weights to the Subtensor blockchain.

---

## 3. Validator Incentive Alignment (dTAO Model)
Under the **Dynamic TAO** framework, validator rewards are intrinsically tied to their accuracy and reputation.

* **V-Trust (Consensus Alignment):** A validator's dividend share is dependent on their **V-Trust** score. If a validator's rankings diverge significantly from the stake-weighted median of the network, their rewards are pruned. This enforces an honest, collective audit of the miners.
* **Alpha Token Yield:** Validators earn rewards in the subnet's native **Alpha token ($\alpha$)**. As the utility of Orchestra grows, the value of the Alpha token relative to TAO increases, creating a compounding "Real Yield" for long-term stakers and delegators.
* **Liquidity Provision:** In 2026, validators also act as "Subnet-Alpha" liquidity providers. By staking into the Orchestra reserve, they stabilize the subnet's economy and ensure the token price reflects the actual demand for decentralized orchestration.

---

## 🛠️ Hardware Requirements
* **CPU:** 16+ vCPUs (High concurrency for auditing multiple miners simultaneously).
* **RAM:** 32GB+ (Required for running local Judge LLMs and maintaining large metagraph states).
* **Networking:** 1Gbps+ (Low latency is critical for real-time verification of cross-subnet proofs).
