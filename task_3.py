import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        # Витягуємо вершину з найменшою відстанню з купи
        current_distance, current_vertex = heapq.heappop(heap)

        # Якщо знайдена відстань більша за вже відому — пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань коротша, оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def main():
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    shortest_paths = dijkstra(graph, 'A')
    print("Найкоротші шляхи від вершини A:")
    print(shortest_paths)


if __name__ == "__main__":
    main()