employees = [
    ('Иванов', 166000),
    ('Сидоров', 180000),
    ('Петров', 155000),
    ('Козлов', 200000),
    ('Смирнов', 175000)
]

# Узел дерева: словарь с ключами 'left','right','name','salary'
def new_node(name, salary):
    return {'left': None, 'right': None, 'name': name, 'salary': salary}

# Вставка в дерево (по ключу salary)
def insert(root, name, salary):
    if root is None:
        return new_node(name, salary)
    if salary < root['salary']:
        root['left'] = insert(root['left'], name, salary)
    else:
        root['right'] = insert(root['right'], name, salary)
    return root

# Обход справа-налево (правый-корень-левый) — даёт убывание зарплаты
def traverse_descending(root, result):
    if root is None:
        return
    traverse_descending(root['right'], result)
    result.append((root['name'], root['salary']))
    traverse_descending(root['left'], result)

# Построение дерева
tree = None
for name, salary in employees:
    tree = insert(tree, name, salary)

# Получение отсортированного списка
sorted_list = []
traverse_descending(tree, sorted_list)

# Вывод
print("Ведомость по убыванию зарплаты:")
for name, salary in sorted_list:
    print(f"{name} - {salary}")