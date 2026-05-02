# 🛡️ Pydantic — Data Validation in Python

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Pydantic](https://img.shields.io/badge/Pydantic-v2.x-red?style=flat)
![FastAPI](https://img.shields.io/badge/Compatible-FastAPI-green?style=flat&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

A structured, hands-on learning repository covering **Pydantic v2** —
the most widely used data validation library in Python, and the
backbone of **FastAPI** backends and **AI/ML pipelines**.

> 📌 Pydantic is used in production by FastAPI, LangChain, and 
> most modern Python AI systems for robust data validation.

---

## 📚 What's Covered

| File | Topic | Description |
|------|-------|-------------|
| `01_why_pydantic.py` | Why Pydantic? | Problem with plain Python dicts vs Pydantic models |
| `02_field_validator.py` | Field Validator | Custom field-level validation using `@field_validator` |
| `3_model_validator.py` | Model Validator | Cross-field validation using `@model_validator` |
| `4_computed_fields.py` | Computed Fields | Auto-calculated fields using `@computed_field` |
| `5_nested_models.py` | Nested Models | Complex data structures with nested Pydantic models |
| `6_serialization.py` | Serialization | Converting models to dict/JSON using `.model_dump()` |

---

## 🎯 Why Pydantic Matters for AI Engineers

Pydantic is not just a validation library — it is the **core foundation**
of modern Python AI/ML development:

- ⚡ **FastAPI** uses Pydantic for all request/response validation
- 🤖 **LangChain** uses Pydantic for structured LLM outputs
- 🔧 **Structured outputs** from GPT/Claude use Pydantic schemas
- 🛡️ **Production AI pipelines** rely on Pydantic for data integrity

---

## 💡 Key Concepts Demonstrated

```python
from pydantic import BaseModel, Field, field_validator, computed_field

class Patient(BaseModel):
    name: str
    age: int = Field(..., ge=0, le=120)
    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18

# ✅ Valid data
patient = Patient(name="John Doe", age=30, email="john@example.com")
print(patient.model_dump())
# {'name': 'John Doe', 'age': 30, 'email': 'john@example.com', 'is_adult': True}

# ❌ Invalid data — Pydantic raises clear error
try:
    Patient(name="Jane", age=-5, email="invalid-email")
except Exception as e:
    print(e)
```

---

## 🔄 Pydantic v1 vs v2 — Key Differences

| Feature | v1 | v2 (This Repo) |
|---------|-----|----------------|
| Validator decorator | `@validator` | `@field_validator` |
| Dict export | `.dict()` | `.model_dump()` |
| JSON export | `.json()` | `.model_dump_json()` |
| Speed | Baseline | **5-50x faster** |
| LangChain support | ✅ | ✅ |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/tashfeen786/Pydantic.git
cd Pydantic

# Install Pydantic v2
pip install pydantic

# Run any example
python 01_why_pydantic.py
python 02_field_validator.py
```

---

## 🏗️ Project Structure

```
Pydantic/
│
├── 01_why_pydantic.py        # Why use Pydantic over plain Python
├── 02_field_validator.py     # Field-level custom validation
├── 3_model_validator.py      # Cross-field model validation
├── 4_computed_fields.py      # Auto-calculated fields
├── 5_nested_models.py        # Complex nested data structures
└── 6_serialization.py        # dict/JSON serialization methods
```

---

## 🛠️ Requirements

- Python 3.8+
- Pydantic 2.x

```bash
pip install pydantic
```

---

## 🔗 Real-World Usage

This knowledge is directly applied in:
- ✅ **FastAPI** — request/response body validation
- ✅ **LangChain** — structured LLM output parsing
- ✅ **AI Pipelines** — validating model inputs/outputs
- ✅ **Backend APIs** — type-safe data handling

---

## 👨‍💻 Author

**Tashfeen Aziz** — AI/ML Engineer & Python Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/tashfeen-aziz-b51361292)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/tashfeen786)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:tashfeen247@gmail.com)

---

⭐ **If you found this helpful, please give it a star!**
