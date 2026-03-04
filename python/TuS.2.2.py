def node(val):
    return {'info': val, 'ptr': None}

def create(arr):
    if not arr:
        return None, None
    head = node(arr[0])
    tail = head
    for v in arr[1:]:
        n = node(v)
        tail['ptr'] = n
        tail = n
    tail['ptr'] = head
    return head, tail

def print_list(head):
    if head is None:
        print()
        return
    cur = head
    while True:
        print(cur['info'], end=' ')
        cur = cur['ptr']
        if cur == head:
            break
    print()

def length(head):
    if head is None:
        return 0
    cnt = 1
    cur = head['ptr']
    while cur != head:
        cnt += 1
        cur = cur['ptr']
    return cnt

def transfer(head1, tail1, head2, tail2, L):
    if L <= 0 or head1 is None:
        return head1, tail1, head2, tail2

    len1 = length(head1)
    if L > len1:
        L = len1
    if L == 0:
        return head1, tail1, head2, tail2

    # Перевод всей первой группы
    if L == len1:
        if head2 is None:
            head2 = head1
            tail2 = tail1
        else:
            tail2['ptr'] = head1
            tail2 = tail1
            tail2['ptr'] = head2
        head1 = None
        tail1 = None
        return head1, tail1, head2, tail2

    # Частичный перевод
    last = head1
    for _ in range(L - 1):
        last = last['ptr']
    next_first = last['ptr']
    last['ptr'] = None
    tail1['ptr'] = next_first
    moved_head = head1
    moved_tail = last
    head1 = next_first

    if head2 is None:
        head2 = moved_head
        tail2 = moved_tail
        tail2['ptr'] = head2
    else:
        tail2['ptr'] = moved_head
        tail2 = moved_tail
        tail2['ptr'] = head2

    return head1, tail1, head2, tail2


g1 = input("Первая группа: ").split()
g2 = input("Вторая группа: ").split()
L = int(input("Число переводимых: "))

head1, tail1 = create(g1)
head2, tail2 = create(g2)

head1, tail1, head2, tail2 = transfer(head1, tail1, head2, tail2, L)

print_list(head1)
print_list(head2)