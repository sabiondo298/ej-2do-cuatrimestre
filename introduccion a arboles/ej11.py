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
            raise ValueError("Error: División por cero.")
        return izq_val / der_val


def evaluate(expression: str):
    # Convierte la expresión RPN a árbol y calcula su resultado
    arbol = inverse_polish_parser(expression)
    return calculate(arbol)


# --- PRUEBAS ---
print(evaluate("4 5 + 5 3 - *"))  # Debería dar 18
print(evaluate("3 5 + 2 *"))      # Debería dar 16
print(evaluate("10 12 3 / -"))    # Debería dar 6.0