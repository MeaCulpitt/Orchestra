## 1. Incentive & Mechanism Design

The goal is to incentivize **Orchestration Intelligence**—the ability to decompose a single user intent into a multi-subnet execution plan.

### Reward Logic
Rewards are split via the standard **41/41/18** model (Miners/Validators/Owners). Emissions are calculated based on the **Orchestration Efficiency Score (OES)**.

### The OES Formula
$$OES = (W_{s} \cdot Speed) + (W_{a} \cdot Accuracy) + (W_{e} \cdot Efficiency)$$

* **$W_{s}$ (Speed):** Total round-trip time from prompt to final synthesis.
* **$W_{a}$ (Accuracy):** Validator assessment of the final output quality.
* **$W_{e}$ (Efficiency):** Minimizing redundant calls to subnets (rewarding "clean" logic).

### Adversarial Discouragement
* **Pipeline Verification:** Miners must submit a `task_pipeline` log. If a miner claims to have used an external subnet but cannot provide the signed response hash from that subnet’s validator, their score for that epoch is zeroed.
* **Synthetic Trap Tasks:** Validators inject "known-answer" complex tasks. If a miner hallucinates or bypasses the sub-steps, they face immediate rank pruning.
