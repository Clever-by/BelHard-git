# datetime

from datetime import datetime, timedelta, date, time

d = date(2005, 7, 14)
t = time(12, 30)

print(datetime.combine(d, t))
# Результат

print(datetime.now())
# Результат

# strptime из string в datetime
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
# Результат

# strftime из datetime в string
dtn = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
print(dtn)
# Результат

print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
# Результат


# End