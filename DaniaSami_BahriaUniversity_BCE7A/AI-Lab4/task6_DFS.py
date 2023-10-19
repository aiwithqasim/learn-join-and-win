#DANIA SAMI AI AND MACHINE LEARNING LAB 04 TASK NO 06 - DFS
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H', 'I'],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

# Starting node for DFS
starting_node = 'A'

print(f"DFS from node {starting_node} :")
visited_nodes = set()
dfs(graph, starting_node, visited_nodes)