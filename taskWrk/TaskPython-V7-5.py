# *** Class


from contextlib import suppress
from contextlib import redirect_stdout

# Менеджеры контекста

# Проблема с кодировкой utf-8, читает файлы только с кодировкой cp1251
# Используем encoding="utf-8": open(encoding="utf-8")
# Используем encoding="ansi": open(encoding="ansi")
# Используем encoding="cp1251": open(encoding="cp1251")

"""
with open('./taskWrk/resource/fileTask-7.txt', encoding="utf-8") as f:
    print(f.read())
    print(f"тип f.read(): {type(f.read())}")
    string = f.read()
    # нет значения
    print(f"тип: {type(string)}\nСодержание файла:\n{string}")
"""

# Обработка через исключения
"""
try:
    f = open('./taskWrk/resource/fileTask-7.txt', encoding="utf-8")
    print(f.read())

except:
    # обработка исключений
    print(f"Except")

finally:
    f.close()
"""

#"""
class OpenidFile:
    
    def __init__(self, textfile):
        self.textfile = textfile
    
    def __enter__(self):
        self.file = open(self.textfile)
        return self.file
    
    def __exit__(self, *args):
        print(args)
        self.file.close()
        
try:
    with OpenidFile('./taskWrk/resource/fileTask-7.txt', "r", encoding="utf-8") as f:
        print(f.read())

except:
    print("Close File, because error: ")
    
"""
try:
    1/0

except ValueError as VE:
    #pass
    Err = VE
    print(Err, type(VE))

with suppress(ZeroDivisionError):
    1/0
"""

# Добавить в конец тетска
with redirect_stdout(open('./taskWrk/resource/fileTask-7.txt', 'a', encoding="utf-8")):
    print('Context Managers')


# End