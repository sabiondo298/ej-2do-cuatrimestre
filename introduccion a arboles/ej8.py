# Volvé a escribir la expresión del punto anterior pero con las otras notaciones 
# vistas en clase (notación polaca y notación polaca inversa). 
# ¿Qué algoritmos de recorrido deberías usar para mostrar en pantalla 
# el árbol del punto anterior expresado en cada una de ellas (incluyendo la notación infija)?


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# Crear los nodos
raiz = Nodo("*")

division = Nodo("/")
suma = Nodo("+")
resta = Nodo("-")

dos1 = Nodo(2)
seis = Nodo(6)
ocho = Nodo(8)

nueve = Nodo(9)
dos2 = Nodo(2)


# Conectar los nodos
raiz.izquierdo = division
raiz.derecho = resta

division.izquierdo = suma
division.derecho = ocho

suma.izquierdo = dos1
suma.derecho = seis

resta.izquierdo = nueve
resta.derecho = dos2


# Notación infija - IN-ORDER
def in_order(nodo):
    if nodo is not None:
        in_order(nodo.izquierdo)
        print(nodo.valor, end=" ")
        in_order(nodo.derecho)


# Notación polaca - PRE-ORDER
def pre_order(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        pre_order(nodo.izquierdo)
        pre_order(nodo.derecho)


# Notación polaca inversa - POST-ORDER
def post_order(nodo):
    if nodo is not None:
        post_order(nodo.izquierdo)
        post_order(nodo.derecho)
        print(nodo.valor, end=" ")


print("Notación infija:")
in_order(raiz)

print("\nNotación polaca:")
pre_order(raiz)

print("\nNotación polaca inversa:")
post_order(raiz)