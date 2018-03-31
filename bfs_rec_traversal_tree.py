class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight + 1

def printlevelorder(root):
    h = height(root)
    for i in range( 1 , h+1):
        printgivenlevel(root,i)

def printgivenlevel(root , level):
    if root is None:
        return None
    if level == 1:
        print(root.val)
    elif level > 1:
        printgivenlevel(root.left, level - 1)
        printgivenlevel(root.right,level - 1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)        
