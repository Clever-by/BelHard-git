# *** OOP

# Декоратор @property. Аксессоры

class Person:
    
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
        #self.full_name = fn + ' ' + ln
        self.full_name = f'Chelovek: {fn} {ln}'
    
    @property # Обернуть декоратором
    def get_full_name(self):
         return f'Chelovek: {self.fn} {self.ln}'

    @get_full_name.setter # Обернули в декоратор с аксессором
    def set_full_name(self, val):
        self.fn, self.ln = val.split()
    
    
chel = Person('Shell', 'Oil')
chel.fn = 'Andrey'
#chel.set_full_name('Angelina Jolie') # до оборачивания декоратора с аксессором

print('Chelovek:', chel.fn, chel.ln)
print(chel.full_name)
#print(chel.get_full_name()) # до оборачивания в декоратор @property
print(chel.get_full_name) # После оборачивания в декоратор, обращаемся как к переменной

chel.set_full_name = 'Kari Cool'
print(chel.get_full_name)





# End