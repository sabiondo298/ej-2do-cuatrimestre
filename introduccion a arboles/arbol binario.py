import os
import collections 
from collections import deque

class Arbol_binario:
    class Node:
        def __init__(self, valor):
            self.valor = valor
            self.izquierda = None
            self.derecha = None

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = self.Node(valor)
            return

        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = self.Node(valor)
                    return
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = self.Node(valor)
                    return
                actual = actual.derecha

    def inorder(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return
        self._inorder(nodo)

    def _inorder(self, nodo):
        if nodo is None:
            return
        self._inorder(nodo.izquierda)
        print(nodo.valor, end=" ")
        self._inorder(nodo.derecha)

    def preorder(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return
        self._preorder(nodo)

    def _preorder(self, nodo):
        if nodo is None:
            return
        print(nodo.valor, end=" ")
        self._preorder(nodo.izquierda)
        self._preorder(nodo.derecha)

    def postorder(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return
        self._postorder(nodo)

    def _postorder(self, nodo):
        if nodo is None:
            return
        self._postorder(nodo.izquierda)
        self._postorder(nodo.derecha)
        print(nodo.valor, end=" ")


if __name__ == "__main__":
    os.system("cls")
    arbol = Arbol_binario()
    for valor in ["A", "B", "C", "D", "E", "F", "G"]:
        arbol.insertar(valor)

    print("Recorrido inorder:")
    arbol.inorder()
    print("\n")

    print("Recorrido preorder:")
    arbol.preorder()
    print("\n")

    print("Recorrido postorder:")
    arbol.postorder()
    print()
