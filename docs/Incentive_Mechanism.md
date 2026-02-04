## ⚙️ Incentive & Mechanism Design

The Orchestra subnet utilizes a market-driven incentive model built on the **Yuma Consensus** and **Dynamic TAO (dTAO)**. Our goal is to reward miners who demonstrate superior "Orchestration Intelligence."

### The OES Formula (Orchestration Efficiency Score)
To ensure the subnet provides high utility, we calculate rewards using three core vectors:
$$OES = (W_{s} \cdot Speed) + (W_{a} \cdot Accuracy) + (W_{e} \cdot Efficiency)$$

* **Speed ($W_{s}$):** Measures the round-trip latency. In an agentic economy, speed is the difference between a tool being useful or obsolete.
* **Accuracy ($W_{a}$):** Validated via a Consensus Judge LLM that compares the miner's final output against a reference standard.
* **Efficiency ($W_{e}$):** Miners are penalized for redundant API calls. We reward "clean" logic that solves tasks using the minimum necessary expert nodes.

### dTAO Economic Flywheel
Under the dTAO 2026 upgrade, SN-Orchestra functions as an independent Automated Market Maker (AMM). 
* **Alpha Token ($\alpha$):** Emissions are paid in the subnet's native token.
* **Staking Signals:** As demand for orchestration grows, stakers swap TAO for Orchestra Alpha, increasing the subnet's emission share from the global 1 TAO/block pool.

### Adversarial Discouragement
* **Signed Receipts:** Miners must submit cryptographically signed hashes from the validators of the subnets they utilized (e.g., a signature from an SN62 validator).
* **Pruning:** Low-performing miners are automatically deregistered once the 256 UID slots are filled, ensuring a constant "survival of the fittest."
