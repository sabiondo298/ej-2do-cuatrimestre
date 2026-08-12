# Implementá en Python una clase Nodo que se asemeje a un nodo de un árbol

class Node:
    def __init__(self, data):
        self.data = data
        self.izquierda = None
        self.derecha = None


mi_nodo = Node("20")
print(mi_nodo.data)
