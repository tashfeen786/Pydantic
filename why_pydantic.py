

def insert_patient_data(name: str, age: int):
    if name == str and age == int:
        print(name)
        print(age)
        print('inserted into database')
    else:
        raise TypeError('Incorrect data type')
    
def update_patient_data(name: str, age: int):
    if name == str and age == int:
        print(name)
        print(age)
        print('Update patient data in database')
    else:
        raise TypeError('Incorrect Datatype ')