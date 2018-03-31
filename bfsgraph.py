def bfs_connected_component(graph,start):    
    explored=[]
    queue=[start]
    while queue:
        #pop the first node in queue
        node = queue.pop(0)
        if node not in explored:
            #
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


