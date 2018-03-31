graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs_rec(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            print(visited)
            dfs_rec(graph,n,visited)
        return visited
#dfs_rec(graph1,'A',[])
