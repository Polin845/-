def S(lst):
    ''' Описание функции S: функция сортирует список
    Описание аргуметов: lst - передаваемый список'''

    for i in range(len(lst) - 1):
        low_index = i
        for j in range(i + 1, len(lst)):
            if float(lst[low_index][4]) > float(lst[j][4]):
                low_index = j
        lst[low_index], lst[i] = lst[i], lst[low_index]
    return lst


cars = []    # создаём список для данных о всех машинах
with open('cars.csv') as f:
    for a in f:
        a = [i for i in a.strip().split(';')]
        cars.append(a)

print(cars[0])
cars = S(cars[1:])    # сортируем список всех машин по пробегу
for i in cars[:3]:
    print(f'{i[2]} {i[3]}; Цвет: {i[-1]}; Пробег: {i[-2]}; Цена: {i[0]}')