# *** Сериализация


import json

# json

# метод dump - получает объект и файл
# метод dumps - получает строку 

# Метод load загружает файл
# Метод loads загружает строку

data = {    
  "text": "string",
  "int_list": [1, 2, 3],
  "none": None
}

#print(json.dumps(data))

with open(r"./taskWrk/dump/dump_json", "w", encoding="utf-8") as wFile:
    json.dump(data, wFile)
    #file.close()
    
with open(r"./taskWrk/dump/dump_json", "r", encoding="utf-8") as rFile:
    # Метод loads загружает строку
    #dump_load = rFile.read()
    #j_data = json.loads(dump_load)
    
    # Метод load загружает файл
    j_data = json.load(rFile) 
    
    #file.close()


print(j_data)
#print(j_data['text'])

l = j_data['int_list']

# Перебераем словарь
for num in l:
    print(f"Position: {num}")


# End