import heapq

def dijkstra(graph, start):
    # Inicialización
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]  # (distancia, nodo)
    
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        
        # Si la distancia actual es mayor a la registrada, se ignora
        if current_dist > shortest_paths[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            # Si encontramos un camino más corto, lo actualizamos
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Ejemplo de uso
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Mostrar resultados
for node, distance in shortest_paths.items():
    print(f"Distancia más corta de {start_node} a {node}: {distance}")
