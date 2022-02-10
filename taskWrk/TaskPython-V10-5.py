# *** Сериализация


import yaml

# yaml

# метод dump - получает объект и файл
# метод dumps - получает строку 

# Метод load загружает файл
# Метод loads загружает строку

data = {    
  "text": "string",
  "int_list": [1, 2, 3],
  "none": None
}

#print(yaml.dump(data))

#dump_all - пишет только индекс
#print(yaml.dump_all(data))

with open(r"./taskWrk/dump/dump_yaml", "w", encoding="utf-8") as file:
    yaml.dump(data, file)
    file.close()
 
with open(r"./taskWrk/dump/dump_yaml", "r", encoding="utf-8") as file:
    # Метод loads загружает строку
    dump_load = file.read()
    y_data = yaml.load(dump_load)
    
    # Метод load загружает файл
    #y_data = yaml.load(file) 
    
    file.close()


print(type(y_data))

# Если использовать метод "load" при загрузку из файла и как текст
print(y_data)
print(y_data['none'])

# Если использовать метод "load_all" при загрузку, как текст
#for st in y_data:
    #print(f"rez: {st['text']}")


# End