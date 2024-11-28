class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Creating the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# The tree structure:
#        1
#       / \
#      2   3
#     / \
#    4   5

# Functions for traversal (already defined earlier)
def pre_order(node):
    if not node:
        return
    print(node.value, end=" ")
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.value, end=" ")
    in_order(node.right)

def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.value, end=" ")

# Forward order
def find_path(root, target):
    path = []
    def dfs(node, target):
        if not node:
            return False
        path.append(node.value)
        if target == node.value:
            return True
        if dfs(node.left, target) or dfs(node.right, target):
            return True
        path.pop()
        return False

    if dfs(root, target):
        return path
    return None

# Reverse order
def find_path(root, target):
    if root is None:
        return []
    if root.value == target:
        return [root.value]
    left_path = find_path(root.left, target)
    right_path = find_path(root.right, target)

    if left_path:
        return left_path + [root.value]
    if right_path:
        return right_path + [root.value]

    return []

print(find_path(root, 0))

# Testing the traversals
print("Pre-order traversal:")
pre_order(root)  # Output: 1 2 4 5 3

print("\nIn-order traversal:")
in_order(root)  # Output: 4 2 5 1 3

print("\nPost-order traversal:")
post_order(root)  # Output: 4 5 2 3 1
