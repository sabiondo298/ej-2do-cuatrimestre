class Nodo:
    def __init__(self, data):
        self.data = data
        self.izquierdo = None
        self.derecho = None


A = Nodo("A")
B = Nodo("B")
C = Nodo("C")
D = Nodo("D")
E = Nodo("E")
F = Nodo("F")
G = Nodo("G")

A.izquierdo = B
A.derecho = F

B.izquierdo = C
B.derecho = E

C.izquierdo = D

F.derecho = G