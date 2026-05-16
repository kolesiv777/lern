def node(val):
    return {'info': val, 'ptr': None}

def create(arr):
    head = None
    tail = None
    for v in arr:
        n = node(v)
        if head is None:
            head = n
            tail = n
        else:
            tail['ptr'] = n
            tail = n
    return head

def print_list(head):
    cur = head
    while cur:
        print(cur['info'], end=' ')
        cur = cur['ptr']
    print()

def copy_list(head):
    if not head:
        return None
    new_head = node(head['info'])
    cur = new_head
    old = head['ptr']
    while old:
        n = node(old['info'])
        cur['ptr'] = n
        cur = n
        old = old['ptr']
    return new_head

def find_candidates(head):
    res = []
    pos = 0
    prev = None
    cur = head
    nxt = head['ptr'] if head else None
    while nxt:
        if prev:
            d1 = cur['info'] - prev['info']
            d2 = cur['info'] - nxt['info']
            if d1 % 2 == 0 and d2 % 2 == 0:
                res.append((pos, cur['info']))
        prev = cur
        cur = nxt
        nxt = nxt['ptr']
        pos += 1
    return res

def move_to_front(head, val):
    if not head or head['info'] == val:
        return head
    prev = None
    cur = head
    while cur and cur['info'] != val:
        prev = cur
        cur = cur['ptr']
    if not cur:
        return head
    prev['ptr'] = cur['ptr']
    cur['ptr'] = head
    return cur

def transpose_to_front(head, val):
    if not head or head['info'] == val:
        return head
    target = head
    while target and target['info'] != val:
        target = target['ptr']
    if not target:
        return head
    while target != head:
        p = head
        while p['ptr'] != target:
            p = p['ptr']
        p['info'], target['info'] = target['info'], p['info']
        target = p
    return head

# Основная программа
arr = input("Введите целые числа через пробел: ").split()
if len(arr) < 3:
    print("Ошибка: нужно хотя бы 3 элемента")
    exit()

nums = [int(x) for x in arr]
head = create(nums)

cand = find_candidates(head)
if not cand:
    print("Нет элемента, у которого разность с обоими соседями чётная")
    exit()

idx, val = max(cand, key=lambda x: x[1])
print(f"Найденный элемент: {val} на позиции {idx}")

h1 = copy_list(head)
h1 = move_to_front(h1, val)
print("1) После перестановки в начало (move‑to‑front): ", end='')
print_list(h1)

h2 = copy_list(head)
h2 = transpose_to_front(h2, val)
print("2) После транспозиции в начало: ", end='')
print_list(h2)