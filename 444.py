cars = []    # создаём список для данных о всех машинах
with open('cars.csv') as f:
    for a in f:
        a = [i for i in a.strip().split(';')]
        cars.append(a)

cars = cars[1:]
for i in range(len(cars)):
    if float(cars[i][-2]) < 70_000.0:
        cars[i][0] = str(int(cars[i][0]) * 0.88)    # замеяем старую цену на цену со скидкойй

print(cars[:10])