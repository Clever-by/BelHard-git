# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle

from random import randint
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

#print(yaml.dump(data))
pos_in = randint(1,2)

with open(r"./homeWork/dump/dump_yaml", "w", encoding="utf-8") as wFile:
    # Вариант 1
    if pos_in == 1:
        yaml.dump(data, wFile)
    
    # Вариант 2
    if pos_in == 2:
        wFile.write(yaml.dump(data))
        
#wFile.close()

print(f"Вариант загрузки: {pos_in}")
pos_out = randint(1,2)

with open(r"./homeWork/dump/dump_yaml", "r", encoding="utf-8") as rFile:
    # Вариант 1. Получаем на вход файл
    if pos_out == 1:
        #y_data = yaml.load(rFile) 
        y_data = yaml.safe_load(rFile) 
        #file.close()

    # Вариант 2. Получаем на вход файл
    elif pos_out == 2:
        dump_load = rFile.read()
        y_data = yaml.load(dump_load)
        

    else:
        y_data = ""
        
#rFile.close()

print(f"Вариант выгрузки: {pos_out}")
    
print(f"Тип словаря из файла: {type(y_data)}")

print(f"Словарь: {y_data}")
print(f"Имя {y_data['name']}. Возраст {y_data['age']}")
print(f"Имя ребенка {y_data['children']['name']}. Возраст {y_data['children']['age']}")

#End