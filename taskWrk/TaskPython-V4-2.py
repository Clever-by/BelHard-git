# *** Collection Python


# *** Генератор

a2 = [1, 2, 3, -6, 10, 3, 20, 4, 3]

def positive(value):
    return value % 2 == 0 and value > 0


print('Output collection enumerate a2(i(j)): ', list(enumerate(a2)))
col_num = [i[0] for i in enumerate(a2) if i[1]==3]
# i[1] - Индекс по значению, т.к. i[0,1] состоит из индекса и значения
print(col_num)
col_num = [ind for ind, item in enumerate(a2) if positive(item)] #==4]
print(col_num)


print('Output collection a2: ', a2)
sq = [i**2 for i in a2]
print('Collection a2 in squares: ', sq)
#
print('Output collection a2: ', a2)
#
m = [i-2 for i in a2]
print('Collection a2 in minus-2: ', m)
#
print('Output collection a2: ', a2)
ab = [abs(i) for i in a2]
print('Collection a2 in ABS: ', ab)
#
print('Output collection a2: ', a2)
ot1 = [i+100 for i in a2 if i >= 5 and i < 100]
print('Collection a2 in Other If1: ', ot1)
#
print('Output collection a2: ', a2)
ot2 = []
#ot2 = [(if i < 0 i+200) for i in a2]
print('Collection a2 in Other If2: ', ot2)


# End