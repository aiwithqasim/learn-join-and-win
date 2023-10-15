from collections import deque
#Graph representation as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': [''],
    'E': ['8'],
    'F': ['C']
}
def bfs(graph, start):
    queue = deque([start])
    result = []
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            queue.extend(graph[node])
    return result


def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            result.append(node)
            stack.extend(graph[node][::-1])
            visited.add(node)
    return result
