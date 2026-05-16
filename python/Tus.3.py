def make_node(key, rec):
    return {'key': key, 'rec': rec, 'left': None, 'right': None}

def copy_tree(node):
    if node is None:
        return None
   
    new_node = make_node(node['key'], node['rec'])
    new_node['left'] = copy_tree(node['left'])
    new_node['right'] = copy_tree(node['right'])
    return new_node

def build(keys, recs=None):
   
    if not keys:
        return None

    if recs is None:
        recs = [f"rec_{k}" for k in keys]
   

    root = make_node(keys[0], recs[0])

    for key, rec in zip(keys[1:], recs[1:]):
        p = root
        q = None

        while p is not None:
            q = p
            if key < p['key']:
                p = p['left']
            else:
                p = p['right']

        new_node = make_node(key, rec)

        if key < q['key']:
            q['left'] = new_node
        else:
            q['right'] = new_node

    return root

keys = [14, 18, 6, 21, 1, 13, 15]
recs = ["A", "B", "C", "D", "E", "F", "G"] 

root = build(keys, recs)

copyr = copy_tree(root)

print(root['key'])
print(copyr['key'], "\n")

copyr['key'] = 100
print(root['key'])
print(copyr['key'])