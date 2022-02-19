# *** CSV


import csv


# поумолчанию разделитель ","

"""
with open(r"./taskWrk/resource/csvFile.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f'Вывод строки: {" ".join(row)}')
        #print(f"Вывод списка: {row}")
"""
"""    
with open(r"./taskWrk/resource/csvFile.csv", "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        #print(f"Вывод массива построчно: {line}")
        print(f'ИФ: {line["first_name"]}, {line["last_name"]}')
        
"""
#"""
with open(r"./taskWrk/resource/csvFile.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)
    
print(f"Вывод массива: {data}")
#"""
#"""
# Параметр delimiter - указывает, какой использовать разделитель
with open(r"./taskWrk/resource/csvOut.csv", "w", encoding="utf-8") as wfile:
    writer = csv.DictWriter(wfile, fieldnames=list(data[0].keys()), delimiter=';')
    writer.writeheader()
    writer.writerows(data)

# Параметр delimiter - указывает, какой использовать разделитель
with open(r"./taskWrk/resource/csvOut.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=';')
    data = list(reader)
    
print(f"Вывод массива: {data}")
#"""

# End