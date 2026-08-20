class PriorityQueue:
    def __init__(self, tabla=None):
        self.tabla = [] if tabla is None else tabla

    def insert(self, nodo):
        posicion = 0
        while (posicion < len(self.tabla)
               and self.tabla[posicion].priority >= nodo.priority):
            posicion += 1
        self.tabla.insert(posicion, nodo)


    class Nodo:
        def __init__(self, data, priority):
            self.data = data
            self.priority = priority


priority_queue = PriorityQueue(tabla=[])
nodo1 = priority_queue.Nodo("Wachin2", 2)
nodo2 = priority_queue.Nodo("Wachin1", 1)
nodo3 = priority_queue.Nodo("Wachin3", 3)
priority_queue.insert(nodo1)
priority_queue.insert(nodo2)
priority_queue.insert(nodo3)

print("Cola ordenada por prioridad:")
for nodo in priority_queue.tabla:
    print(f"Data: {nodo.data}, Priority: {nodo.priority}")


