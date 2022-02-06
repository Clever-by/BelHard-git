# Регулярные выражения

# Регулярные выражения - шаблон поиска подстрок в тексте

import re

letter = '''
Hi, everyone.
...
Sergey Pashkevich
Sezh@belhard.edu
'''

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+'
print(re.search(email_pattern, letter))

s = 'string01 string02   string05      string06 \t string09'
# \w - все символы
# \s - символы "Пробелы"
print(re.split(r'\s+', s))


info = 'Database, user=sadmin, pass=<cool_passw0rds>'
# скрыть "password"
print(re.sub(r'\<.+\>', '<*****>', info))


# End