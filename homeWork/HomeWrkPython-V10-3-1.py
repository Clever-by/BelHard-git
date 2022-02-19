# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle

from random import randint
import json
from operator import index

data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {'age': 3,
         'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}

#print(json.dumps(data))
pos_in = randint(1,2)

with open(r"./homeWork/dump/dump_json", "w", encoding="utf-8") as wFile:
    # Вариант 1
    if pos_in == 1:
        json.dump(data, wFile)
        
    if pos_in == 2:
        # Вариант 2
        wFile.write(json.dumps(data))
    
    #wFile.close()

print(f"Вариант загрузки: {pos_in}")
pos_out = randint(1,2)

with open(r"./homeWork/dump/dump_json", "r", encoding="utf-8") as rFile:
    # Вариант 1. Получаем на вход файл
    if pos_out == 1:
        j_data = json.load(rFile) 
        
    # Вариант 2. Обралатываем строки из файла
    elif pos_out == 2:
        dump_load = rFile.read()
        j_data = json.loads(dump_load)
        
    else:
        j_data = ""

#rFile.close()

print(f"Вариант выгрузки: {pos_out}")

print(f"Словарь: {j_data}")
print(f"Имя {j_data['name']}. Возраст {j_data['age']}")

print(f"{j_data['children']} Тип списка: {type(j_data['children'])}")
l = dict(j_data['children'][0])
print(f"Имя ребенка {l['name']}. Возраст {l['age']}")


#End