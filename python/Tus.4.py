import math

def ls(a, x):
    c = 0
    for i in range(len(a)):
        c += 1
        if a[i] == x:
            return True, i, c
    return False, -1, c

def bs(a, x):
    c = 0
    L, R = 0, len(a) - 1
    while L <= R:
        m = (L + R) // 2
        c += 1
        if a[m] == x:
            return True, m, c
        elif a[m] < x:
            L = m + 1
        else:
            R = m - 1
    return False, -1, c

def iss(a, x, st=None):
    n = len(a)
    if st is None:
        st = int(math.sqrt(n)) or 1
    tbl = []
    for i in range(0, n, st):
        tbl.append((a[i], i))
    c = 0
    idx = 0
    while idx < len(tbl) and tbl[idx][0] <= x:
        c += 1
        idx += 1
    if idx == 0:
        low = 0
    else:
        low = tbl[idx-1][1]
    if idx == len(tbl):
        high = n
    else:
        high = tbl[idx][1]
    for i in range(low, high):
        c += 1
        if a[i] == x:
            return True, i, c
    return False, -1, c

arr = list(map(int, input("Массив: ").split()))
arr.sort()
print("Отсорт.:", arr)
x = int(input("Искомое: "))

f, i, c = ls(arr, x)
print(f"Линейный: найд={f}, инд={i}, сравнений={c}")
f, i, c = bs(arr, x)
print(f"Бинарный: найд={f}, инд={i}, ссравнений={c}")
f, i, c = iss(arr, x)
print(f"Инд-посл: найд={f}, инд={i}, сравнений={c}")