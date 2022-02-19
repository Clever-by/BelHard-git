# *** Сериализация


import json
from typing import Optional 
from pydantic import BaseModel

class Child(BaseModel):
    
    name: str
    age: int
    
    
class Person(BaseModel):
    
    name: str
    age: int
    children: list
    #children: Optional[list[Child]] = None
    
    @property
    def is_sov(self):
        return self.age >= 18

#b = Person(name='Bob', age='58')
#print(b)
#print(b.json())
    
data = {
    "name": "Bob",
    "age": '58',
    'children': [{
        "name": "Nancy",
        "age": '5'
    },{
        "name": "Alisa",
        "age": '9'
    }]
}

p = Person(**data)
print(p)
#print(type(p))
print(p.json())
#print(type(p.json()))

#"""
with open(r"./taskWrk/dump/dumpClass_json", "w", encoding="utf-8") as wFile:
    json.dump(p.json(), wFile)
    #wFile.close()
    
with open(r"./taskWrk/dump/dumpClass_json", "r", encoding="utf-8") as rFile:
    # Метод loads загружает строку
    #dump_load = rFile.read()
    #j_data = json.loads(dump_load)
    
    # Метод load загружает файл
    j_data = json.load(rFile) 
    
    rFile.close()

print(j_data)
print(type(j_data))
#"""

# End