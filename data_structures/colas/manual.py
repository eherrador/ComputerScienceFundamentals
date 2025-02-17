class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Queue:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def enqueue(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.final:
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo
        if self.frente is None:
            self.frente = nuevo_nodo
        self.tamaño += 1

    def dequeue(self):
        if self.frente is None:
            return None  # Cola vacía
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamaño -= 1
        return valor

    def peek(self):
        return None if self.frente is None else self.frente.valor

    def is_empty(self):
        return self.frente is None

    def size(self):
        return self.tamaño

# 🚀 Prueba de Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # 10
print(queue.peek())  # 20
print(queue.is_empty())  # False
print(queue.size())  # 2
