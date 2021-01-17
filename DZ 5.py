my_list = [4, 2, 6, 3, 8]
my_list.sort(reverse=True)
print(my_list)
num = int(input('Введите число: '))
for i in range(len(my_list)):
    if(my_list[i] == num):
        my_list.insert(i+1, num)
        break
    elif (my_list[0] < num):
        my_list.insert(0, num)
    elif (my_list[-1] > num):
        my_list.append(num)
    elif (my_list[i] > num and my_list[i + 1] < num):
        my_list.insert(i + 1, num)
print(f"текущий список - {my_list}")

