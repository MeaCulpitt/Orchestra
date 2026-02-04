import bittensor as bt
import numpy as np
from typing import List
from orchestra.protocol import OrchestraSynapse

def reward(synapse: OrchestraSynapse) -> float:
    """
    Calculates the reward for a single miner based on the OES formula:
    OES = (Wr * Reasoning) + (Wf * Fidelity) + (Wu * Utility)
    """
    # 1. Fidelity Score (Cryptographic Proof)
    # Check if the miner provided valid hashes from external subnets
    fidelity = 0.0
    if synapse.task_pipeline and len(synapse.task_pipeline) > 0:
        # Simplified check: rewards miners for having non-empty, well-formed logs
        # In production, this would verify signatures against the external metagraph
        fidelity = 1.0 

    # 2. Reasoning Score (Logical Consistency)
    # Evaluates if the reasoning_path exists and meets length/logic requirements
    reasoning = 0.0
    if synapse.reasoning_path and len(synapse.reasoning_path) > 50:
        reasoning = 1.0

    # 3. Utility Score (Synthesized Quality)
    # Evaluates the quality of final_completion
    utility = 0.0
    if synapse.final_completion and len(synapse.final_completion) > 100:
        utility = 1.0

    # OES Weighted sum (40% Reasoning, 30% Fidelity, 30% Utility)
    return (0.4 * reasoning) + (0.3 * fidelity) + (0.3 * utility)

def get_rewards(self, synapse: OrchestraSynapse, responses: List[OrchestraSynapse]) -> np.ndarray:
    """
    Vectorized reward calculation for a set of miner responses.
    """
    return np.nan_to_num(np.array([reward(response) for response in responses]), nan=0.0)
