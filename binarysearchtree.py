class Node:
  def __init__(self, val=0):
    self.val = val
    self.left = None
    self.right = None

# Print node values of tree through inorder traversal
def inorder(root):
  if not root:
    return

  inorder(root.left)
  print(root.val)
  inorder(root.right)

# Insert a node into a tree
def insert(root, val):
  if not root:
    return Node(val=val)

  if val < root.val:
    root.left = insert(root.left, val)
  elif root.val < val:
    root.right = insert(root.right, val)

  return root

# Search for a node with a given value
def search(root, val):
  if not root or root.val == val:
    return root

  if val < root.val:
    return search(root.left, val)

  return search(root.right, val)

# Find the node with smallest value in a given tree
def findMinValueNode(root):
  current = root
  if not current:
    return None

  while current.left:
    current = current.left

  return current

# Remove a node from the tree
# Node to be deleted has 3 Cases
# 1. No child (leaf)
# 2. One child
# 3. Two children
def remove(root, val):
  if not root:
    return root

  if val < root.val:
    root.left = remove(root.left, val)
  elif root.val < val:
    root.right = remove(root.right, val)
  else:
    # right child or no child
    if not root.left:
      temp = root.right
      root = None
      return temp
    
    # left child
    elif not root.right:
      temp = root.left
      root = None
      return temp
    
    # left and right child
    temp = findMinValueNode(root.right)

    root.val = temp.val

    root.right = remove(root.right, temp.val)

    return root
