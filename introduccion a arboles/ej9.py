# Implementá una función que se llame inverse_polish_parser que tome como argumento 
# un string como el siguiente “4 5 + 5 3 - *” y que devuelva un árbol que represente dicha expresión. 
# Para esto, usá un Stack (podés armar uno rápido de cero o reutilizar el que ya tenías hecho del cuatrimestre pasado). 
# Si querés asegurarte de haberlo hecho bien, podés recorrer y printear el árbol que armó tu 
# parser con el método post-order y debería devolver el mismo string que le pasaste a la función.

class Nodo:
    def __init__(self, data):
        self.data = data
        self.izquierdo = None
        self.derecho = None


def inverse_polish_parser(expression: str) -> Nodo:
    tokens = expression.split()
    pila = []
    operadores = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operadores:
            derecho = pila.pop()
            izquierdo = pila.pop()
            
            nodo_operador = Nodo(token)
            nodo_operador.izquierdo = izquierdo
            nodo_operador.derecho = derecho
            
            pila.append(nodo_operador)
        else:
            try:
                val = int(token)
            except ValueError:
                try:
                    val = float(token)
                except ValueError:
                    val = token
            
            pila.append(Nodo(val))

    return pila.pop()


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
            raise ValueError("División por cero.")
        return izq_val / der_val


def recorrer_post_order(nodo: Nodo, resultado=None):
    if resultado is None:
        resultado = []
    
    if nodo is not None:
        recorrer_post_order(nodo.izquierdo, resultado)
        recorrer_post_order(nodo.derecho, resultado)
        resultado.append(str(nodo.data))
        
    return resultado


if __name__ == "__main__":
    expresion_original = "4 5 + 5 3 - *"

    arbol_raiz = inverse_polish_parser(expresion_original)

    expresion_reconstruida = " ".join(recorrer_post_order(arbol_raiz))

    resultado = calculate(arbol_raiz)

    print("Expresión original:    ", expresion_original)
    print("Recorrido Post-Order:  ", expresion_reconstruida)
    print("¿El árbol es correcto?:", expresion_original == expresion_reconstruida)
    print("Resultado de la cuenta:", resultado)