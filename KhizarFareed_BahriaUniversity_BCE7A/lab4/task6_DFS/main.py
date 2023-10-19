graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(graph,start):
    stack,path =[start],[]
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        print(vertex)
        for neighbour in graph[vertex]:
            stack.append(neighbour)
    return path


dfs(graph,'A')
