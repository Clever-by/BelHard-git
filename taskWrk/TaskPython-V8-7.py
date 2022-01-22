# *** OOP

# Абстрактные классы

#from abc import ABC, abstractmethod
import abc

class BaseCar(abc.ABC):

    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed
    
    @abc.abstractmethod
    def ride(self):
        print('Drive')
        return 'Smart Car'
        pass


class Car(BaseCar):
    
    def __init__(self, wheels, max_speed, passenger):
        BaseCar.__init__(self, wheels, max_speed)
        self.passenger = passenger
    
    def ride(self):
        print('Small Car')
        return 'Vroom-vroom'
        
#car1 = BaseCar(4, 220)
#a1 = car1.ride()
#print(a1)

car2 = Car(4, 250, 5)
a2 = car2.ride()
print('Количество пассажиров =', car2.passenger)

# End