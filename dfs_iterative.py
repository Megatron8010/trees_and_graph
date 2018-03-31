def dfs(graph,start):
    explored = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                stack.append(neighbour)
        else:
            continue
    return explored

#graph = {'A': set(['B', 'C']),
   #      'B': set(['A', 'D', 'E']),
    #     'C': set(['A', 'F']),
     #    'D': set(['B']),
      #   'E': set(['B', 'F']),
       #  'F': set(['C', 'E'])}
            
        
            
