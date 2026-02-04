import bittensor as bt
import orchestra

def get_version() -> int:
    """Returns the version of the subnet code."""
    return 100 # Represents v1.0.0

def check_version(self):
    """Logs the version and potentially forces updates."""
    bt.logging.info(f"SN-Orchestra Version: {orchestra.__version__}")
