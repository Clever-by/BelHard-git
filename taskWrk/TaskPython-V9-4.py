# OS

import os

#os.environ - словарь переменных окружения
#print(os.environ)

#os.chdir(path) - смена текущей директории.

#os.getcwd() - текущая рабочая директория.
print(f'Link: {os.getcwd()}')

#os.listdir(path=”.”) - список файлов и директорий в папке
list_dir = os.listdir(".")
#print(list_dir)
for dir in list_dir:
    if dir != '.gitignore' and dir != 'index.html':
        #pass
        print(dir)

for str_child in os.listdir("."):
    print(f"list dir: {str_child}, {type(str_child)}")
#os.mkdir(path) - создаёт директорию
new_dir = 'new'
#os.mkdir(new_dir)

#os.remove(path) - удаляет путь к файлу
#os.remove(new_dir)

#os.system(command) - исполняет системную команду, возвращает код её завершения
#print(os.system("ls -la"))


# End