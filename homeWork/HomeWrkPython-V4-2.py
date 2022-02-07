#список словарей, которые содержат поля имя, возраст, пол.

persons = [
    {
        "name": "Anna",
        "age": 25,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Keanu",
        "age": 57,
        "gender": "male"
    }, {
        "name": "Angelina",
        "age": 46,
        "gender": "female"
    }, {
        "name": "Alex",
        "age": 42,
        "gender": "male"
    }, {
        "name": "Cortana",
        "age": 25,
        "gender": "female"
    }, {
        "name": "Carlsen",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Jan",
        "age": 31,
        "gender": "male"
    },{
        "name": "Florentino",
        "age": 74,
        "gender": "male"
    },{
        "name": "Angelina",
        "age": 16,
        "gender": "female"
    },{
        "name": "Alex",
        "age": 22,
        "gender": "male"
    },{
        "name": "Alex",
        "age": 15,
        "gender": "male"
    },{
        "name": "Alex",
        "age": 55,
        "gender": "female"
    },{
        "name": "Jan",
        "age": 30,
        "gender": "male"
    }
]

def firstSymbol(string1):
    l = list(string1)
    f_sym = l[0]
    return f_sym

def unique(list_in):
    list_out = list(set(list_in))
    return list_out

print("Словать состоит из:", len(persons), "записей")

count_ls = len(persons)

num = 0
count_f = 0
count_m = 0
count_w = 0
count_adult = 0
count_m_old = 0
str_name = ''
str_all = ''
l_all = list()
l_name = list()
l_nameMax = list()
l_nameSort = list()
l_age = list()
s_age = set()
s_name = set()


while count_ls > num:
    #print(persons[num]['name'])
    if persons[num]['gender'] == 'female':
        count_f += 1
    
    if persons[num]['gender'] == 'male':
        count_m += 1    
    
    if int(persons[num]['age']) > 17:
        count_adult += 1
    
    if  int(persons[num]['age']) > 35 and persons[num]['gender'] == 'male' and firstSymbol(persons[num]['name']) == 'F':
        count_m_old += 1
        l_name.append(persons[num]['name'])
        str_name = str_name + ' ' + str(persons[num]['name'])
        print(persons[num]['name'])      
        
    #print(persons[num]['name'])
    l_all.append(persons[num]['name'])
    str_all = str_all + ' ' + str(persons[num]['name'])
    
    l_age.append(persons[num]['age']) 
    
    num += 1

print("В списках", count_m, "мужчин", "В списках", count_f, "женщин")
print("Совершеннолетних", count_adult, "человек, кому есть 18 лет")

# Сортировка по алфавиту
l_all.sort()
# Вывод списка
print("Список всех имен из словаря по алфавиту:", l_all)
# Вывод строки
print("Список всех имен строкой из словаря, как в словаре:", str_all)

# Вывод строки
print("Имена мужчин:", l_name, "старше 35 лет и имя начинается на 'F' всего =", count_m_old)
# Вывод списка
print("Имена мужчин:", str_name, "старше 35 лет и имя начинается на 'F' всего =", count_m_old)
l_age.sort()
print("Список всех возрастов:", l_age, "Количество:", len(l_age))
l_age = unique(l_age)
l_age.sort()
print("Списсок всех уникальных возрастов:", l_age, "Количество:", len(l_age))

l_nameSort = unique(l_all)
l_nameSort.sort()
num = 0
while len(l_nameSort) > num:
    #print(l_nameSort[num])
    count_w = 0
    for item in l_all:
         if item == l_nameSort[num]:
             count_w += 1
    
    #print(count_w)
    l_nameMax.append(str(count_w)+" "+l_nameSort[num])
    num += 1

l_nameMax.sort()
l_nameMax.reverse()

print("Три самых встречающиеся имени:", l_nameMax[0:3])




