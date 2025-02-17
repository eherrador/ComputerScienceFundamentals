from collections import deque

queue = deque()  # Crear cola

queue.append(10)  # enqueue(10)
queue.append(20)  # enqueue(20)
queue.append(30)  # enqueue(30)

print(queue.popleft())  # dequeue() → 10
print(queue.popleft())  # dequeue() → 20
print(queue)  # deque([30])
