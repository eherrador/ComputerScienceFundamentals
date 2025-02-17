import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random

def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}  # Para reconstruir caminos

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, previous_nodes

def generate_random_graph(num_nodes, num_edges, weight_range=(1, 10)):
    G = nx.Graph()
    
    for i in range(num_nodes):
        G.add_node(i)
    
    while len(G.edges) < num_edges:
        u, v = random.sample(range(num_nodes), 2)
        weight = random.randint(*weight_range)
        G.add_edge(u, v, weight=weight)

    return G

def plot_graph(G, shortest_paths, previous_nodes, start_node):
    pos = nx.spring_layout(G, seed=42)  # Fijamos la disposición
    plt.figure(figsize=(10, 7))

    # Dibujar nodos y etiquetas
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=700, font_size=10)
    
    # Dibujar pesos de las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Resaltar el camino más corto
    target_nodes = shortest_paths.keys()
    for node in target_nodes:
        if previous_nodes[node] is not None:
            path_edge = (previous_nodes[node], node)
            nx.draw_networkx_edges(G, pos, edgelist=[path_edge], edge_color="red", width=2.5)

    plt.title("Dijkstra: Caminos Más Cortos desde el Nodo Inicial")
    plt.show()

# Generar un grafo aleatorio
num_nodes = 10
num_edges = 15
G = generate_random_graph(num_nodes, num_edges)

# Convertir a diccionario de adyacencia con pesos
graph_dict = {node: {neighbor: G[node][neighbor]['weight'] for neighbor in G.neighbors(node)} for node in G.nodes}

# Aplicar Dijkstra desde el nodo 0
start_node = 0
shortest_paths, previous_nodes = dijkstra(graph_dict, start_node)

# Graficar resultado
plot_graph(G, shortest_paths, previous_nodes, start_node)
