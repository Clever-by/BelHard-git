# Считать кол-во дней до нового года (при помощи параметра --hours, так же часов)

from datetime import datetime
import random
import argparse

class Holidays:
    
    d14feb = datetime.strptime("14.02.2022 00:00", "%d.%m.%Y %H:%M")    
    d23feb = datetime.strptime("23.02.2022 00:00", "%d.%m.%Y %H:%M")    
    d08mar = datetime.strptime("08.03.2022 00:00", "%d.%m.%Y %H:%M")
    d01jan = datetime.strptime("01.01.2022 00:00", "%d.%m.%Y %H:%M")
    new_year = datetime.strptime("01.01.2023 00:00", "%d.%m.%Y %H:%M")

    important_dates = ['1 January', 'New Year', '14 February', '23 February', '8 March']

    def __init__(self, holiday: str):
        self.holiday = holiday
        
    def getHoliday(self):
        if self.holiday == '14 February':
            if self.d14feb > datetime.now():
                day_rez = (f'До {self.holiday} осталось {self.d14feb - datetime.now()}')
            else:
                day_rez = (f'Праздник {self.holiday} прошел {self.d14feb - datetime.now()}')
        
        elif self.holiday == '23 February':
            if self.d23feb > datetime.now():
                day_rez = (f'До {self.holiday} осталось {self.d23feb - datetime.now()}')
            else:
                day_rez = (f'Праздник {self.holiday} прошел {self.d23feb - datetime.now()}')
            
        elif self.holiday == '8 March':
            if self.d08mar > datetime.now():
                day_rez = (f'До {self.holiday} осталось {self.d08mar - datetime.now()}')
            else:
                day_rez = (f'Праздник {self.holiday} прошел {self.d08mar - datetime.now()}')
                
        elif self.holiday == '1 January':
            day_rez = (f'{self.holiday} был {self.d01jan - datetime.now()}')
            
        elif self.holiday == 'New Year':
            day_rez = (f'До нового года осталось: {self.new_year - datetime.now()}')
        
        else:
            day_rez = (f'В нашем календаре нет такого праздника')
        
        return day_rez
        

parser = argparse.ArgumentParser(description='Calendar with holidays')
parser.add_argument('-d', '--setday', type=int, default=10, help='Holiday')
args = parser.parse_args()

print(f'setday={args.setday}')

#Запускать через командную строку из директории, где лежит файл:

# python .\HomeWrkPython-V9-1.py --help
# python .\HomeWrkPython-V9-1.py -h
# d - опционально
# python .\HomeWrkPython-V9-1.py -d 10
# 0 - '1 January', 
# 1 - 'New Year', 
# 2 - '14 February', 
# 3 - '23 February', 
# 4 - '8 March',
# 5 - 'Other day'
# 10 - 'Random'


#count_day = len(Holidays.important_dates)
#random_day = random.randint(0,count_day-1)

#print(Holidays.important_dates[random.randint(0, len(Holidays.important_dates)-1)])

if args.setday >= 0 and args.setday < 5:
    holiday = Holidays.important_dates[args.setday]
    
elif args.setday == 5:
    holiday = 'Other'
    
else:
    holiday = Holidays.important_dates[random.randint(0, len(Holidays.important_dates)-1)]

#how_many_day = Holidays('8 March')
how_many_day = Holidays(holiday)

print(how_many_day.getHoliday())


#End