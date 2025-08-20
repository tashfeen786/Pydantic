# Pydantic
Pydantic Learning Repository

This repository contains my learning journey and practice examples with Pydantic
 — a data validation and settings management library for Python.

🚀 About

Pydantic is used to enforce type hints at runtime and provides user-friendly errors when data is invalid. It ensures data integrity by validating, parsing, and converting input into expected types.

This repo demonstrates:

✅ Why Pydantic

✅ Field validation 

✅ Nested models 

✅ serialization (dict(), json())

✅ Custom validators (@validator, @field_validator)


🔧 Installation & Setup

Clone the repo and install dependencies:

git clone https://github.com/your-username/pydantic-learning.git
cd pydantic-learning

📝 Example Usage
from pydantic import BaseModel, Field

class Patient(BaseModel):
    name: str
    age: int = Field(..., ge=0, le=120)
    email: str

# ✅ Valid data
patient = Patient(name="John Doe", age=30, email="john@example.com")
print(patient.dict())

# ❌ Invalid data
try:
    Patient(name="Jane", age=-5, email="janeexample.com")
except Exception as e:
    print(e)

🎯 Key Learnings

Strong data validation with clear error messages

Built-in support for parsing JSON & environment variables

Cleaner, safer, and more maintainable Python code

📌 Requirements

Python 3.8+

Pydantic 2.x

Install with:

pip install pydantic

🤝 Contributing

This repo is mainly for personal learning, but suggestions and improvements are welcome.

📜 License

This project is open-source under the MIT License.
