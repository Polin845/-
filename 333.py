cars = []    # создаём список для данных о всех машинах
with open('cars.csv') as f:
    for a in f:
        a = [i for i in a.strip().split(';')]
        cars.append(a)

car = str(input())    # принимаем данные от пользователя
man, color = car.split()
good = []    # список с параметрами подошедших машин
for i in cars:   # ищем машины подхоящие под входные данные
    if i[2] == man and i[-1] == color:
        good.append(i)

if len(good) == 0:
    print('По данным параметрам ничего не найдено')
else:
    print(f'По вашему запросу: {man} {color} найдены следующие варианты:')
    for i in range(len(good)):    # перебираем подошедшие машины
        print(f'{i + 1}.  {good[i][2]} {good[i][3]} цена {good[i][0]}, пробег данной машины составляет {good[i][-2]}')
