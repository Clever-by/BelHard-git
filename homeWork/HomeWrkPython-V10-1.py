# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle


list_str = 'Основной механизм работы с содержимым файлов - встроенная функция open'

with open(r"./homeWork/resourse/textList.txt", "w", encoding="utf-8") as f:
    f.write(list_str)

    f.close()


with open(r"./homeWork/resourse/textList.txt", "r", encoding="utf-8") as f:
    string = f.read()

    f.close()

print(string)


#End