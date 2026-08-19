lista_ejemplo = [2, 5, 7, 4, 1, 2, 3, 10]

class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, lista):
        for i in lista:
            if self.size == 0:
                self.heap.append(i)
                self.size += 1
                print(f"Heap: {self.heap}")
            else:
                self.heap.append(i)
                self.size += 1
                swap = True
                while swap:
                    if self.heap[self.size // 2] > i:
                        self.heap[self.size // 2], self.heap[self.size] = self.heap[self.size], self.heap[self.size // 2] #swap
                        print(f"Heap: {self.heap}")
                        swap = True
                    swap = False
                    print(f"Heap: {self.heap}")

my_min_heap = MinHeap()

my_min_heap.insert(lista_ejemplo)
