# *** Class

# Менеджеры контекста

with open('taskWrk\\resource\p.txt') as f:
    print(f.read())


# versus
"""
try:
    f = open(‘list.txt’)
    print(f.read())
except:
    # обработка исключений
finally:
    f.close()
"""
        
        
# End