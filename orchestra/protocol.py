import bittensor as bt
from typing import List, Optional, Dict
import pydantic

class OrchestraSynapse(bt.Synapse):
    """
    The SN-Orchestra communication protocol.
    
    Attributes:
        objective: A string describing the complex multi-step task.
        context: Optional metadata for task constraints (e.g., max latency).
        task_pipeline: Filled by the miner. A log of external subnet calls and their hash proofs.
        reasoning_path: Filled by the miner. A textual explanation of the chosen routing strategy.
        final_completion: Filled by the miner. The synthesized final answer for the user.
    """

    # Request fields (set by Validator)
    objective: str = pydantic.Field(..., allow_mutation=False)
    context: Optional[Dict] = pydantic.Field(None, allow_mutation=False)

    # Response fields (filled by Miner)
    task_pipeline: Optional[List[Dict]] = None
    reasoning_path: Optional[str] = None
    final_completion: Optional[str] = None

    def deserialize(self) -> str:
        """Returns the final answer from the miner."""
        return self.final_completion
