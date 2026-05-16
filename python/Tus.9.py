A = [44, 55, 12, 42, 94, 18, 6, 67]
B = A[:]                           # копия А

n = len(B)
h = n                         # начальный шаг
while h > 0:
    for i in range(h, n):
        temp = B[i]
        j = i
        while j >= h and B[j-h] > temp:
            B[j] = B[j-h]
            j -= h
        B[j] = temp
    h //= 2

print("Массив A:", A)
print("Массив B (возрастание):", B)