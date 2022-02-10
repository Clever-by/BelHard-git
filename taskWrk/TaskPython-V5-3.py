# *** Операторы break, continue


for num in range(5):
    if num == 3:
        continue
    print(num)
print("Оператор continue:", num**2)

for num in range(5):
    if num == 3:
        break
    print(num)
print("Оператор break:", num**2)


# End