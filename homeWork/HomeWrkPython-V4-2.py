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


print("Словать состоит из:", len(persons), "записей")
count_ls = len(persons)

num = 0
count_f = 0
count_m = 0
count_adult = 0
count_m_old = 0
l = list()

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
        print(persons[num]['name'])      
    
    #print(persons[num]['name'])
    l.append(persons[num]['name'])
    
    num += 1

print("В списках", count_m, "мужчин")
print("В списках", count_f, "женщин")
print("Список всех имен из словаря:", "\n", l)
print("Совершеннолетних", count_adult, " человек, кому есть 18 лет")
print("Имена мужчин",  count_m_old, "старше 35 лет и с именем на 'F'")