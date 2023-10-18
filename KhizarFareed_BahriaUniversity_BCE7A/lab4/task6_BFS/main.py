graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph,start):
    queue,path =[start],[]
    while queue:
        vertex = queue.pop(0)
        if vertex in path:
            continue
        path.append(vertex)
        print(vertex)
        for neighbour in graph[vertex]:
            queue.append(neighbour)
    return path


bfs(graph,'A')
