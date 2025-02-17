class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Stack:
    def __init__(self):
        self.tope = None
        self.tamaño = 0

    def push(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamaño += 1

    def pop(self):
        if self.tope is None:
            return None  # Stack vacío
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        self.tamaño -= 1
        return valor

    def peek(self):
        return None if self.tope is None else self.tope.valor

    def is_empty(self):
        return self.tope is None

    def size(self):
        return self.tamaño

# 🚀 Prueba de Stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # 30
print(stack.peek())  # 20
print(stack.is_empty())  # False
print(stack.size())  # 2