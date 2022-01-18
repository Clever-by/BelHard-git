# *** Class

# Менеджеры контекста

"""
with open('taskWrk\\resource\list.txt') as f:
    print(f.read())
"""

# Обработка через исключения

"""
try:
    f = open('taskWrk\\resource\list.txt')
    print(f.read())
except:
    # обработка исключений
finally:
    f.close()
"""

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
    with OpenidFile('taskWrk\\resource\list.txt') as f:
        print(f.read())

except:
    print("Close File, because error: ")
    

from contextlib import suppress

try:
    1/0

except ValueError as VE:
    #pass
    Err = VE
    print(Err, type(VE))

with suppress(ZeroDivisionError):
    1/0
    

from contextlib import redirect_stdout

with redirect_stdout(open('taskWrk\\resource\stdout.txt', 'a')):
    print('Context Managers')

# End