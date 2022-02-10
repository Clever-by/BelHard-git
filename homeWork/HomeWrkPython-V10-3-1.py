# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle


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

print(json.dumps(data))

with open(r"./homeWork/dump/dump_json", "w", encoding="utf-8") as file:
    json.dump(data, file)
    file.close()
    
with open(r"./homeWork/dump/dump_json", "r", encoding="utf-8") as file:
    j_data = json.load(file) 
    
    file.close()


print(f"Словарь: {j_data}")
print(f"Имя {j_data['name']}. Возраст {j_data['age']}")

print(f"{j_data['children']} Тип списка: {type(j_data['children'])}")
l = dict(j_data['children'][0])
print(f"Имя ребенка {l['name']}. Возраст {l['age']}")


#End