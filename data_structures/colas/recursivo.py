class QueueRecursiva:
    def __init__(self):
        self.queue = []

    def enqueue(self, valor):
        if not self.queue:
            self.queue.append(valor)
        else:
            front = self.queue.pop(0)
            self.enqueue(valor)
            self.queue.insert(0, front)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

# 🚀 Prueba de Queue Recursiva
queue_r = QueueRecursiva()
queue_r.enqueue(10)
queue_r.enqueue(20)
queue_r.enqueue(30)

print(queue_r.dequeue())  # 10
print(queue_r.dequeue())  # 20
