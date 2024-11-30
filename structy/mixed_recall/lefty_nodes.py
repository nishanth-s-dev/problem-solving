class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def lefty_nodes(root):
  values = []
  traverse(root, 0, values)
  return values

def traverse(root, level, values):
  if root is None:
    return

  if len(values) == level:
    values.append(root.val)

  traverse(root.left, level + 1, values)
  traverse(root.right, level + 1, values)

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

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

res = lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]
print(res)
