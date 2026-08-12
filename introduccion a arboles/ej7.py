# Explicá con tus palabras qué es una expresión aritmética,
# y utilizá un árbol para representar la siguiente expresión: [(2 + 6) / 8] * (9 - 2).

# Una expresión aritmética es una combinación de números y operaciones matemáticas, 
# como suma, resta, multiplicación y división, que permite obtener un resultado.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


raiz = Nodo("*")

division = Nodo("/")
suma = Nodo("+")
resta = Nodo("-")

dos1 = Nodo(2)
seis = Nodo(6)
ocho = Nodo(8)

nueve = Nodo(9)
dos2 = Nodo(2)



raiz.izquierdo = division
raiz.derecho = resta

division.izquierdo = suma
division.derecho = ocho

suma.izquierdo = dos1
suma.derecho = seis

resta.izquierdo = nueve
resta.derecho = dos2