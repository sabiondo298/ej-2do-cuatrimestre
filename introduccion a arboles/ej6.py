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

def in_order(nodo):
    if nodo is not None:
        in_order(nodo.izquierdo)
        print(nodo.valor)
        in_order(nodo.derecho)


def pre_order(nodo):
    if nodo is not None:
        print(nodo.valor)
        pre_order(nodo.izquierdo)
        pre_order(nodo.derecho)


def post_order(nodo):
    if nodo is not None:
        post_order(nodo.izquierdo)
        post_order(nodo.derecho)
        print(nodo.valor)


def level_order(raiz):
    cola = [raiz]

    while cola:
        nodo = cola.pop(0)

        print(nodo.valor)

        if nodo.izquierdo is not None:
            cola.append(nodo.izquierdo)

        if nodo.derecho is not None:
            cola.append(nodo.derecho)