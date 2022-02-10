# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle


import yaml

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

print(yaml.dump(data))

with open(r"./homeWork/dump/dump_yaml", "w", encoding="utf-8") as file:
    yaml.dump(data, file)
    file.close()
    
with open(r"./homeWork/dump/dump_yaml", "r", encoding="utf-8") as file:
    dump_load = file.read()
    y_data = yaml.load(dump_load)
    
    file.close()


print(f"Тип словаря из файла: {type(y_data)}")

print(f"Словарь: {y_data}")
print(f"Имя {y_data['name']}. Возраст {y_data['age']}")
print(f"Имя ребенка {y_data['children']['name']}. Возраст {y_data['children']['age']}")

#End