# Implementa una función recursiva llamada calculate que tome 
# como argumento un árbol (a través un nodo) que represente una expresión aritmética y que devuelva su resultado. 
# Probala con distintos árboles.

class Nodo:
    def __init__(self, data):
        self.data = data
        self.izquierdo = None
        self.derecho = None


def calculate(nodo: Nodo):
    if nodo.izquierdo is None and nodo.derecho is None:
        return nodo.data

    izq_val = calculate(nodo.izquierdo)
    der_val = calculate(nodo.derecho)

    if nodo.data == '+':
        return izq_val + der_val
    elif nodo.data == '-':
        return izq_val - der_val
    elif nodo.data == '*':
        return izq_val * der_val
    elif nodo.data == '/':
        if der_val == 0:
            raise ValueError("Error: División por cero.")
        return izq_val / der_val
    else:
        raise ValueError(f"Operador desconocido: {nodo.data}")


# Árbol 1: (3 + 5) * 2
arbol1 = Nodo('*')
arbol1.izquierdo = Nodo('+')
arbol1.izquierdo.izquierdo = Nodo(3)
arbol1.izquierdo.derecho = Nodo(5)
arbol1.derecho = Nodo(2)

print("Árbol 1 -> (3 + 5) * 2 = ", calculate(arbol1))


# Árbol 2: 10 - (12 / 3)
arbol2 = Nodo('-')
arbol2.izquierdo = Nodo(10)
arbol2.derecho = Nodo('/')
arbol2.derecho.izquierdo = Nodo(12)
arbol2.derecho.derecho = Nodo(3)

print("Árbol 2 -> 10 - (12 / 3) = ", calculate(arbol2))


# Árbol 3: 42
arbol3 = Nodo(42)

print("Árbol 3 -> 42 = ", calculate(arbol3))


# Árbol 4: ((7 - 2) * 4) + 6
arbol4 = Nodo('+')
arbol4.izquierdo = Nodo('*')
arbol4.izquierdo.izquierdo = Nodo('-')
arbol4.izquierdo.izquierdo.izquierdo = Nodo(7)
arbol4.izquierdo.izquierdo.derecho = Nodo(2)
arbol4.izquierdo.derecho = Nodo(4)
arbol4.derecho = Nodo(6)

print("Árbol 4 -> ((7 - 2) * 4) + 6 = ", calculate(arbol4))