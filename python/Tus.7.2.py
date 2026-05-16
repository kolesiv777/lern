students = [
    {'name': 'Иванов', 'exam1': 5},
    {'name': 'Петрова', 'exam1': 3},
    {'name': 'Сидоров', 'exam1': 4},
    {'name': 'Козлова', 'exam1': 5},
    {'name': 'Новиков', 'exam1': 3}
    
]

# Сортировка методом прямого выбора по полю 'exam1'
n = len(students)
for i in range(n - 1):
    minidx = i
    for j in range(i + 1, n):
        if students[j]['exam1'] < students[minidx]['exam1']:
            minidx = j
    students[i], students[minidx] = students[minidx], students[i]

# Вывод результата
print("Студенты по возрастанию оценки за 1-й экзамен:")
for st in students:
    print(f"{st['name']}: {st['exam1']}")