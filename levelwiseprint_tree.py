class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val =key
def traversal(root):
    thislevel = [root]
    while thislevel:
        print()
        nextlevel = []
        for n in thislevel:
            print(n.val,end="   ")
            if n.left is not None:
                nextlevel.append(n.left)
            if n.right is not None:
                nextlevel.append(n.right)
            thislevel = nextlevel
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)    
