import json
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

# 1. Define the exact model used by the validator (Sync this with the Subnet Spec)
class OrchestraStandardSchema(BaseModel):
    """
    Standardized schema for Mechanism 1. 
    Miners must match this exactly to receive a high Integrity Score.
    """
    topic: str = Field(..., description="The primary subject of the trend")
    sentiment_score: float = Field(..., ge=-1.0, le=1.0)
    sources: List[int] = Field(..., min_length=1, description="List of Subnet UIDs used")
    confidence: Optional[float] = 0.5
    timestamp: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

    class Config:
        str_strip_whitespace = True
        extra = "forbid"  # Prevents points loss for sending unrequested data

# 2. The Dry-Run Validation Logic
def run_dry_run(miner_output_raw: str):
    """
    Simulates the Validator's check on your output.
    """
    print("--- 🔬 Starting Local Integrity Check ---")
    
    try:
        # Step 1: Check if it's valid JSON
        parsed_json = json.loads(miner_output_raw)
        print("✅ JSON Format: Valid")

        # Step 2: Validate against Pydantic model
        validated_data = OrchestraStandardSchema.model_validate(parsed_json)
        print("✅ Schema Alignment: Perfect")
        print(f"📦 Payload Ready: {validated_data.topic} (Score: {validated_data.sentiment_score})")
        
        return True

    except json.JSONDecodeError:
        print("❌ Error: Output is not a valid JSON string.")
    except ValidationError as e:
        print(f"❌ Error: Schema Validation Failed!")
        for error in e.errors():
            print(f"   └─ Field '{'.'.join(str(l) for l in error['loc'])}': {error['msg']}")
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")
    
    return False

# 3. Example Usage for Testing
if __name__ == "__main__":
    # Example of a "Passing" payload
    good_payload = '{"topic": " Decentralized Compute ", "sentiment_score": 0.85, "sources": [1, 13], "timestamp": "2026-02-06T12:00:00Z"}'
    
    # Example of a "Failing" payload (wrong date format)
    bad_payload = '{"topic": "AI", "sentiment_score": 5.0, "sources": [], "timestamp": "Friday 12pm"}'

    print("\n[TEST 1: Valid Data]")
    run_dry_run(good_payload)

    print("\n[TEST 2: Invalid Data]")
    run_dry_run(bad_payload)
