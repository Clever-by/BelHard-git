# *** OOP

# Полиморфизм

class Horse:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def run(self):
        print(f'Horse {self.name} running')


class Pegasus(Horse):
    

    def run(self):
        print(f'Pegasus {self.name} running')
    
    def fly(self):
        print(f'{self.name} flying')


pegasus = Pegasus('white', 'Pegas')
kon = Horse('black', 'Kon')

horses = [kon, pegasus]

for horse in horses:
    horse.run()

#pegasus.run()
#kon.run()



# End