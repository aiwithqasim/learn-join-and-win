#DANIA SAMI AI AND MACHINE LEARNING LAB 04 TASK NO 06 - BFS
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

starting_node = 'A'

print(f"BFS from node {starting_node} :")
bfs(graph, starting_node)