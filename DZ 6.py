products = {'название': '', 'стоимость': '', 'количество': '', 'ед.': ''}
analisis = {'название': [], 'стоимость': [], 'количество': [], 'ед.': []}
dgs = []
num_prod = 0

while True:
    action = input('Если Вы хотите ввести товар, нажмите "V". Если выхотите сделать анализ, нажмите "A". Для завершения работы, нажмите "Q": ').upper()
    num_prod += 1
    if(action == 'V'):
        for i in products.keys():
            products[i] = input(f'Введите {i} товара:')
            analisis[i].append(products[i])
    dgs.append((num_prod, products))
    if(action =='A'):
        for key, value in analisis.items():
            print(f'{key}: {value}')
    if (action == 'Q'):
        break


