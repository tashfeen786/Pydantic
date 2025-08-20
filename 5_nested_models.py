from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class patient(BaseModel):

    name:str
    gender: str
    age : int
    address: Address

address_dict = {'city': 'Khaplu', 'state': 'Gilgit Baltistan', 'pin': '4567'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Tashfeen', 'gender': ' male', 'age' : '23', 'address': address1}

patient1 = patient(**patient_dict)

temp = patient1.model_dump()

print(type(temp))
