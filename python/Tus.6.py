import random

def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def iscomposite(n):
    return n > 1 and not isprime(n)

def maketree(key):
    return [key, None, None]

def searchandinsert(root, key):
    p = root
    q = None
    while p is not None:
        q = p
        if key == p[0]:
            return root, p
        if key < p[0]:
            p = p[1]
        else:
            p = p[2]
    v = maketree(key)
    if q is None:
        root = v
    else:
        if key < q[0]:
            q[1] = v
        else:
            q[2] = v
    return root, v

def searchanddelete(root, key):
    q = None
    p = root
    while p is not None and p[0] != key:
        q = p
        if key < p[0]:
            p = p[1]
        else:
            p = p[2]
    if p is None:
        return root, None
    if p[1] is None:
        v = p[2]
    elif p[2] is None:
        v = p[1]
    else:
        t = p
        v = p[2]
        s = v[1]
        while s is not None:
            t = v
            v = s
            s = v[1]
        if t != p:
            t[1] = v[2]
            v[2] = p[2]
        v[1] = p[1]
    if q is None:
        root = v
    else:
        if p == q[1]:
            q[1] = v
        else:
            q[2] = v
    return root, p

def inordercollect(root, result):
    if root is not None:
        inordercollect(root[1], result)
        result.append(root[0])
        inordercollect(root[2], result)

choice = input("Сгенерировать 15 случайных чисел? (y/n): ").strip().lower()
if choice == 'y':
    numbers = [random.randint(-99, 99) for _ in range(15)]
    print("Случайные числа:", numbers)
else:
    inp = input("Введите 15 целых чисел через пробел: ")
    numbers = list(map(int, inp.split()))
    if len(numbers) != 15:
        numbers = (numbers + [0]*15)[:15]
        print("Используются первые 15 чисел (дополнены нулями):", numbers)
    else:
        print("Введённые числа:", numbers)

root = None
for num in numbers:
    root, _ = searchandinsert(root, num)

res = []
inordercollect(root, res)
print(root[0])
print("Начальное дерево (отсортировано):", res)


key = int(input("Введите число для поиска: "))
if not iscomposite(key):
    print("Число не является составным.")
else:
    p = root
    found = False
    while p is not None:
        if key == p[0]:
            found = True
            break
        if key < p[0]:
            p = p[1]
        else:
            p = p[2]
    if found:
        print("Число найдено. Удаляем.")
        root, _ = searchanddelete(root, key)
    else:
        print("Число не найдено. Вставляем.")
        root, _ = searchandinsert(root, key)
    res = []
    inordercollect(root, res)
    print("Дерево после операции:", res)