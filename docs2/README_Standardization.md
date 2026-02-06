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
