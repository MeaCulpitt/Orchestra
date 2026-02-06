# 🛠️ Miner Guide: Mastering the JSON Standardization Layer

To succeed on **Mechanism 1 (JSON Standardization)**, miners must provide data that perfectly matches the `target_schema` provided in the `OrchestraSynapse`. In 2026, the industry standard for this is **Pydantic V2**.

Miners who fail schema validation receive a **Data Integrity Score ($W_d$) of 0** for that epoch. Follow this guide to ensure 100% compliance.

---

## 1. Why Pydantic?
Pydantic ensures your miner is "Type Safe." Instead of manually parsing strings, you define a **Data Model**. Pydantic handles:
* **Type Coercion:** Automatically converting a string `"100"` to an integer `100`.
* **Validation:** Ensuring required fields (like `source_uid`) are present.
* **Serialization:** Exporting clean, standardized JSON every time.

---

## 2. Implementation: The Transformation Pipeline
When your miner receives disparate data from external subnets, use the following pattern to standardize it.

### Step A: Define the Model
```python
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class StandardizedTrend(BaseModel):
    """The unified format expected by the Orchestra Validator."""
    topic: str = Field(..., description="The primary subject of the trend")
    sentiment_score: float = Field(..., ge=-1.0, le=1.0)
    sources: List[int] = Field(..., description="List of Subnet UIDs used")
    confidence: Optional[float] = 0.5

    @field_validator('topic')
    @classmethod
    def capitalize_topic(cls, v: str) -> str:
        return v.strip().title()
```

## Step B: The Miner's transform Logic

def transform_to_schema(raw_subnet_data: dict, target_model: BaseModel):
    try:
        # Example: Mapping 'raw_val' from SN13 to 'sentiment_score'
        mapped_data = {
            "topic": raw_subnet_data.get("subject"),
            "sentiment_score": raw_subnet_data.get("raw_val"),
            "sources": [raw_subnet_data.get("origin_uid")]
        }
        
        # This will raise a ValidationError if the data is malformed
        standardized_object = target_model(**mapped_data)
        return standardized_object.model_dump_json()
        
    except Exception as e:
        print(f"Standardization Failed: {e}")
        return None
### 3. Top 3 Tips for a Perfect Integrity Score

* **Always Use `model_validate_json()`**: When receiving data from other subnets, use this Pydantic method to catch errors *before* you synthesize your final response.
* **Handle Optional Fields**: If a data source is missing a field, ensure your model has a default value (e.g., `confidence: float = 0.0`) to prevent the entire synapse from failing.
* **Strip Whitespace**: Use Pydantic's `str_strip_whitespace=True` in your model config to prevent "Invisible Character" penalties from validators.

---

### 4. Validator Check Script

Before submitting your response, you can simulate the validator's check locally:

```python
# If this raises no error, your submission is safe.
try:
    validator_model = StandardizedTrend.model_validate_json(miner_output_json)
    print("Validation Successful: Integrity Score Protected.")
except Exception as e:
    print(f"Validation Failed: {e}")

# If this raises no error, your submission is safe.
validator_model = StandardizedTrend.model_validate_json(miner_output_json)
