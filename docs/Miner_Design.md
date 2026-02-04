## 🛠️ Miner Design: The Strategic Manager

Miners on SN-Orchestra act as high-level **Task Dispatchers**. A successful miner doesn't just run code; they manage a "remote workforce" of other subnets.

### Operational Workflow
1.  **Decomposition Layer:** Use a local LLM or SN1 (Apex) to transform a prompt into a set of sequential or parallel steps.
2.  **Market Discovery:** The miner scans the metagraph to find top-performing UIDs in:
    * **SN62 (Ridges):** For code-heavy requirements.
    * **SN64 (Chutes):** For heavy serverless inference.
    * **SN13 (Data Universe):** For real-time data retrieval.
3.  **Hiring & Execution:** The miner sends synapses to these subnets and handles the response.
4.  **Synthesis:** The final result is merged into a cohesive answer for the Orchestra Validator.

### Technical Requirements
* **Hardware:** 8+ vCPUs, 16GB RAM, and high-speed NVMe storage.
* **Networking:** Must maintain 99.9% uptime to avoid validator scoring penalties.
* **Liquidity:** Miners must maintain a small "working capital" of various subnet Alpha tokens to pay for the external services they coordinate.
