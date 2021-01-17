ls_count= int(input("Введите количество элементов списка: "))
ls_list = []
a = 0
while a < ls_count:
    ls_list.append(input('Введите элемент списка: '))
    a += 1

mr = 0
for i in range(int(len(ls_list) / 2)):
    ls_list[mr], ls_list[mr + 1] = ls_list[mr + 1], ls_list[mr]
    mr += 2

print(ls_list)


