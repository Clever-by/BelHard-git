# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle

import json
from pydantic import BaseModel
from random import randint

class Person(BaseModel):
    
    name: str
    age: int
    children: dict

data = {
    'age': 45,
    'name': 'Peter',
    'children': {
        'age': 3,
        'name': 'Alice'
        }
    ,
    'married': True,
    'city': None
}

p = Person(**data)
#print(dict(p))
#print(type(p))
#print(p.json())
#print(type(p.json()))



with open(r"./homeWork/dump/dumpClass_json", "w", encoding="utf-8") as wFile:
    json.dump(dict(p), wFile)
    #wFile.close()
#"""
pos_out = randint(1,2)
with open(r"./homeWork/dump/dumpClass_json", "r", encoding="utf-8") as rFile:
    if pos_out == 1:
        # Метод loads загружает строку
        dump_load = rFile.read()
        j_data = json.loads(dump_load)
    
    if pos_out == 2:
        # Метод load загружает файл
        j_data = json.load(rFile) 
    
    #rFile.close()

#print(j_data)
#print(type(j_data))
print(f"Вариант выгрузки: {pos_out}")
#"""

#"""
print(f"Тип словаря из файла: {type(j_data)}")

print(f"Словарь: {j_data}")
print(f"Имя {j_data['name']}. Возраст {j_data['age']}")
print(f"Имя ребенка {j_data['children']['name']}. Возраст {j_data['children']['age']}")
#"""

#End