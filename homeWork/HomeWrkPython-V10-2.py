# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle


import pickle

def fun():
    print('Function')
    return f"Function 'fun'"

f = fun()

class Str:
    
    str = 'Сеарилизация через pickle'

# Передаем переменную
string = Str.str +": " + f

with open(r"./homeWork/dump/dump_pickle", "wb") as file:
    pickle.dump(string, file)
    file.close()

with open(r"./homeWork/dump/dump_pickle", "rb") as file:
    f_fun = pickle.load(file) 
    file.close()

print(f"Результат переменной из файла: {f_fun}")


#End