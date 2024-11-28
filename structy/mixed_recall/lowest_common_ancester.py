class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor(root, val1, val2):
    path_1 = find_path(root, val1)
    path_2 = find_path(root, val2)
    path_2_set = set(path_2)

    for val in path_1:
        if val in path_2_set:
            return val
    return None


def find_path(root, target):
    if root is None:
        return []

    if root.val == target:
        return [root.val]

    left_path = find_path(root.left, target)
    if left_path:
        return left_path + [root.val]

    right_path = find_path(root.right, target)
    if right_path:
        return right_path + [root.val]

    return []


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

res = lowest_common_ancestor(a, 'd', 'h')  # b
print(res)