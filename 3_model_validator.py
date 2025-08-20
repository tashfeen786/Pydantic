from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    @model_validator( mode ='after')
    def validate_emergency_contact(cls, model):
        if model.age> 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
    
def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('UPdate')

patient_info = {'name': 'Tashfeen', 'email': 'asdf@gmail.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '3456789', 'emergency': '45678'}}

patient1 = patient(**patient_info)

update_patient_data(patient1)