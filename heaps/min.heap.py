class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, data):
        """Agrega un dato y lo mueve hacia arriba hasta conservar el MinHeap."""
        self.heap.append(data)
        self.size += 1
        self._arrange(self.size)

    def delete_at_root(self):
        """Elimina y devuelve el menor elemento del heap."""
        if self.size == 0:
            raise IndexError("No se puede eliminar la raíz de un heap vacío")

        root = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self.sink(1)
        return root

    def delete_at_location(self, location):
        """Elimina y devuelve el elemento de una posición 1-based."""
        if location < 1 or location > self.size:
            raise IndexError("La ubicación no existe en el heap")

        deleted = self.heap[location]
        self.heap[location] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1

        if location <= self.size:
            parent = location // 2
            if location > 1 and self.heap[location] < self.heap[parent]:
                self._arrange(location)
            else:
                self.sink(location)
        return deleted

    def heap_sort(self):
        """Devuelve los elementos ordenados y conserva el heap original."""
        copy = MinHeap()
        for data in self.heap[1:]:
            copy.insert(data)

        sorted_data = []
        while copy.size > 0:
            sorted_data.append(copy.delete_at_root())
        return sorted_data

    def _arrange(self, location):
        """Mueve un elemento hacia arriba mientras sea menor que su padre."""
        while location > 1:
            parent = location // 2
            if self.heap[parent] <= self.heap[location]:
                break
            self.heap[parent], self.heap[location] = (
                self.heap[location],
                self.heap[parent],
            )
            location = parent

    def sink(self, location):
        """Mueve un elemento hacia abajo hasta encontrar su ubicación correcta."""
        while True:
            child = self.minchild(location)
            if child is None or self.heap[location] <= self.heap[child]:
                break
            self.heap[location], self.heap[child] = (
                self.heap[child],
                self.heap[location],
            )
            location = child

    def minchild(self, location):
        """Devuelve la posición del menor hijo, o None si no tiene hijos."""
        left = location * 2
        right = left + 1

        if left > self.size:
            return None
        if right > self.size or self.heap[left] <= self.heap[right]:
            return left
        return right


if __name__ == "__main__":
    values = [2, 5, 7, 4, 1, 2, 3, 10]
    min_heap = MinHeap()

    for value in values:
        min_heap.insert(value)

    print("Heap después de insertar:", min_heap.heap[1:])
    print("Heap sort:", min_heap.heap_sort())
    print("Heap original después de ordenar:", min_heap.heap[1:])
    print("Elemento eliminado de la posición 3:", min_heap.delete_at_location(3))
    print("Heap después de borrar en posición 3:", min_heap.heap[1:])
    print("Raíz eliminada:", min_heap.delete_at_root())
    print("Heap final:", min_heap.heap[1:])
