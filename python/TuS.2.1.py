def node(val):
    return {'info': val, 'ptr': None}

def create(arr):
    head = None
    for v in arr:
        n = node(v)
        if head is None:
            head = n
            tail = n
        else:
            tail['ptr'] = n
            tail = n
    return head

def contains(head, val):
    cur = head
    while cur:
        if cur['info'] == val:
            return True
        cur = cur['ptr']
    return False

def intersection(a, b):
    res = None
    tail = None
    cur = a
    while cur:
        if contains(b, cur['info']) and not contains(res, cur['info']):
            new = node(cur['info'])
            if res is None:
                res = new
                tail = new
            else:
                tail['ptr'] = new
                tail = new
        cur = cur['ptr']
    return res

def print_list(head):
    cur = head
    while cur:
        print(cur['info'], end=' ')
        cur = cur['ptr']
    print()
    
arr1 = list(map(int, input("Введите первый список: ").split()))
arr2 = list(map(int, input("Введите второй список: ").split()))

L1 = create(arr1)
L2 = create(arr2)
L3 = intersection(L1, L2)

print("Общие элементы:")
print_list(L3)