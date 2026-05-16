cars = [
    {'brand': 'BMW', 'deadline': '15.07.1996'},
    {'brand': 'Audi', 'deadline': '20.08.1996'},
    {'brand': 'Aaudi', 'deadline': '20.07.1996'},
    {'brand': 'Mercedes', 'deadline': '31.07.1996'},
    {'brand': 'BMW', 'deadline': '01.09.1996'},
    {'brand': 'Audi', 'deadline': '25.07.1996'},
    {'brand': 'Lada', 'deadline': '10.08.1996'}
]

# Отбираем машины, у которых deadline < 01.08.1996
cutoff = (1996, 8, 1)
filtered = []
for car in cars:
    d, m, y = map(int, car['deadline'].split('.'))
    if (y, m, d) < cutoff:
        filtered.append(car)

# Сортировка методом прямого включения по полю 'brand'
for i in range(1, len(filtered)):
    temp = filtered[i]
    j = i - 1
    while j >= 0 and filtered[j]['brand'] > temp['brand']:
        filtered[j + 1] = filtered[j]
        j -= 1
    filtered[j + 1] = temp

# Вывод результата
print("Машины, которые нужно отремонтировать до 01.08.1996 (по алфавиту марок):")
for car in filtered:
    print(car['brand'])