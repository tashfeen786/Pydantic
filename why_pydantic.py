from pydantic import BaseModel
from typing import List, Dict, Optional

class patient(BaseModel):
    name: str
    age: int
    weight : float
    allergies :Optional[ List[str]]
    contact_detalies : Dict[str, str]

def insert_patient_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_detalies)
    print('inserted into database')
    
patient_info = {'name': 'Tashfeen Aziz', 'age':30, 'weight': 63.6, 'allergies': ['pollen', 'dust'], 'contact_detalies': {'email': 'abc@gmail.com', 'phone': '1234567890'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)