class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        self.root = None
        

class BST:
    def __init__(self, data):
        self.root = None

    def insert(self, data):
        nodo = Node(data)
        if self.root is None:
            self.root = nodo
            return
        current = self.root
        while True:
            if current.data > nodo.data:
                if current.left is None:
                    current.left = nodo 
                    return
                else:
                    current = current.left

            else:
                if  current.data > nodo.data:
                    if current.right is None:
                        current.right = nodo 
                        return
                    else:
                        current = current.right
bst = BST()

bst.insert(5)
bst.insert(4)
bst.insert(3)
        
