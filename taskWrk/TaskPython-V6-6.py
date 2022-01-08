# *** Пространство имён

# locals()
# globals()
# __builtins__

x = 0

#print(f"Global x = {x}")

def f1():
    y = 1
    #print(f"Function y = {y}")
    #print(locals())
    #print(globals())
    #print(__builtins__)
    
    #b = __builtins__
    #g = globals()
    l = locals()
    
    for item in l.items():
        print(item)
    
        
    def f2():
        z = 2
        print(f"Global x = {x}")
        #print(f"Function z = {z}")
        
    f2()

f1()

__builtins__.print('builtins')

# End