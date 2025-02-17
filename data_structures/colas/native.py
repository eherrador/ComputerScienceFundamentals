queue = []  # Crear cola

queue.append(10)  # enqueue(10)
queue.append(20)  # enqueue(20)
queue.append(30)  # enqueue(30)

print(queue.pop(0))  # dequeue() → 10
print(queue.pop(0))  # dequeue() → 20
print(queue)  # [30]
