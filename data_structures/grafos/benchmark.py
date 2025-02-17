import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random
import time
import numpy as np

def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        if current_dist > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

def generate_random_graph(num_nodes, num_edges, weight_range=(1, 10)):
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i)
    
    while len(G.edges) < num_edges:
        u, v = random.sample(range(num_nodes), 2)
        weight = random.randint(*weight_range)
        G.add_edge(u, v, weight=weight)

    return G

def measure_execution_time():
    node_sizes = [10, 50, 100, 200, 500, 1000, 2000]  # Diferentes tamaños de nodos
    edge_factor = 2  # Relación nodos-aristas (E ≈ 2V)
    times = []

    for num_nodes in node_sizes:
        num_edges = num_nodes * edge_factor  # Mantener la proporción de aristas
        G = generate_random_graph(num_nodes, num_edges)
        graph_dict = {node: {neighbor: G[node][neighbor]['weight'] for neighbor in G.neighbors(node)} for node in G.nodes}

        start_node = 0
        start_time = time.time()
        dijkstra(graph_dict, start_node)
        end_time = time.time()
        
        times.append(end_time - start_time)
        print(f"Grafo con {num_nodes} nodos y {num_edges} aristas → Tiempo: {times[-1]:.6f} seg")

    return node_sizes, times

def plot_execution_times(node_sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(node_sizes, times, marker='o', linestyle='-', color='b', label="Tiempo real")
    
    # Aproximación teórica O((V+E) log V)
    theoretical_times = [n * np.log(n) for n in node_sizes]
    theoretical_times = np.array(theoretical_times) / max(theoretical_times) * max(times)  # Normalizar
    plt.plot(node_sizes, theoretical_times, linestyle='--', color='r', label="O((V+E) log V) esperado")

    plt.xlabel("Número de Nodos (V)")
    plt.ylabel("Tiempo de Ejecución (seg)")
    plt.title("Complejidad Temporal del Algoritmo de Dijkstra")
    plt.legend()
    plt.grid(True)
    plt.show()

# Medir tiempos y graficar
node_sizes, times = measure_execution_time()
plot_execution_times(node_sizes, times)
