#!/usr/bin/env python3

array = None
size = 0
topIndex = -1

def PUSH(value):
    global topIndex
    if topIndex < size - 1:
        topIndex += 1
        array[topIndex] = value

def POP():
    global topIndex
    if topIndex >= 0:
        value = array[topIndex]
        topIndex -= 1
        return value
    return None

def EMPTY():
    return topIndex == -1

def Task1():
    global topIndex
    if topIndex >= 1:
        tempArray = [None] * size
        tempTop = -1
        while not EMPTY():
            tempTop += 1
            tempArray[tempTop] = POP()
        PUSH(tempArray[0])
        for i in range(tempTop - 1, 0, -1):
            PUSH(tempArray[i])
        PUSH(tempArray[tempTop])
    print("Задание 1 выполнено")

def Task2():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    for i in range(0, tempTop + 1):
        PUSH(tempArray[i])
    print("Задание 2 выполнено")

def Task3():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    count = tempTop + 1
    if count % 2:
        middle = count // 2
        for i in range(tempTop, -1, -1):
            if i != middle:
                PUSH(tempArray[i])
    else:
        middleFirst = count // 2 - 1
        middleSecond = count // 2
        for i in range(tempTop, -1, -1):
            if i != middleFirst and i != middleSecond:
                PUSH(tempArray[i])
    print("Задание 3 выполнено")

def Task4():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    for i in range(tempTop, -1, -1):
        if i % 2 == 0:
            PUSH(tempArray[i])
    print("Задание 4 выполнено")

def Task5():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    count = tempTop + 1
    if count % 2 == 0:
        insertPosition = count // 2
    else:
        insertPosition = count // 2 + 1
    for i in range(tempTop, -1, -1):
        PUSH(tempArray[i])
        if i == insertPosition:
            PUSH('*')
    print("Задание 5 выполнено")

def Task6():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    minIndex = 0
    for i in range(1, tempTop + 1):
        if tempArray[i]!="*" and tempArray[i] < tempArray[minIndex]:
            minIndex = i
    for i in range(tempTop, -1, -1):
        PUSH(tempArray[i])
        if i == minIndex:
            PUSH(0)
    print("Задание 6 выполнено")

def Task7():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    maxIndex = 0
    for i in range(1, tempTop + 1):
        if tempArray[i]!="*" and tempArray[i] > tempArray[maxIndex]:
            maxIndex = i
    for i in range(tempTop, -1, -1):
        PUSH(tempArray[i])
        if i == maxIndex:
            PUSH(0)
    print("Задание 7 выполнено")

def Task8():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    minIndex = 0
    for i in range(1, tempTop + 1):
        if tempArray[i]!="*" and tempArray[i] < tempArray[minIndex]:
            minIndex = i
    for i in range(tempTop, -1, -1):
        if i != minIndex:
            PUSH(tempArray[i])
    print("Задание 8 выполнено")

def Task9():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    firstValue = tempArray[tempTop]
    for i in range(tempTop, -1, -1):
        if tempArray[i] != firstValue:
            PUSH(tempArray[i])
    print("Задание 9 выполнено")

def Task10():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    lastValue = tempArray[0]
    for i in range(tempTop, -1, -1):
        if tempArray[i] != lastValue:
            PUSH(tempArray[i])
    print("Задание 10 выполнено")

def Task11():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    maxIndex = 0
    for i in range(1, tempTop + 1):
        if tempArray[i]!="*" and tempArray[i] > tempArray[maxIndex]:
            maxIndex = i
    for i in range(tempTop, -1, -1):
        if i != maxIndex:
            PUSH(tempArray[i])
    print("Задание 11 выполнено")

def Task12():
    global topIndex
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    minIndex = 0
    for i in range(1, tempTop + 1):
        if tempArray[i]!="*" and tempArray[i] < tempArray[minIndex]:
            minIndex = i
    for i in range(tempTop, -1, -1):
        if i == minIndex:
            PUSH(0)
        else:
            PUSH(tempArray[i])
    print("Задание 12 выполнено")

def ShowStack():
    if topIndex == -1:
        print("Стек пуст")
        return
    tempArray = [None] * size
    tempTop = -1
    while not EMPTY():
        tempTop += 1
        tempArray[tempTop] = POP()
    print("Текущий стек:", end=" ")
    for i in range(tempTop, -1, -1):
        print(tempArray[i], end=" ")
        PUSH(tempArray[i])
    print()

size = int(input("Введите размер стека: "))
array = [None] * size
topIndex = -1

print(f"Введите {size} элементов стека:")
for i in range(size):
    value = input(f"Элемент {i+1}: ")
    if value.isdigit():
        PUSH(int(value))
    else:
        PUSH(value)

print("\nИсходный стек:")
ShowStack()

while True:
    print("\n1-Первый и последний")
    print("2-Развернуть")
    print("3-Удалить средний")
    print("4-Удалить каждый второй")
    print("5-Вставить *")
    print("6-0 после минимального")
    print("7-0 после максимального")
    print("8-Удалить минимальный")
    print("9-Удалить равные первому")
    print("10-Удалить равные последнему")
    print("11-Удалить максимальный")
    print("12-Заменить минимальный на 0")

    choice = input("Выберите задание: ")

    match choice:
        case '1':
            Task1()
            ShowStack()
        case '2':
            Task2()
            ShowStack()
        case '3':
            Task3()
            ShowStack()
        case '4':
            Task4()
            ShowStack()
        case '5':
            Task5()
            ShowStack()
        case '6':
            Task6()
            ShowStack()
        case '7':
            Task7()
            ShowStack()
        case '8':
            Task8()
            ShowStack()
        case '9':
            Task9()
            ShowStack()
        case '10':
            Task10()
            ShowStack()
        case '11':
            Task11()
            ShowStack()
        case '12':
            Task12()
            ShowStack()
        case _:
            print("Неверный выбор!")
