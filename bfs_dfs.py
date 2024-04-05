graph = {
    "Oardea": ["Zerind", "Sibiu"],
    "Zerind": ["Arad", "Oardea"],
    "Arad": ["Zerind", "Timisoara", "Sibiu"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],
    "Rimnicu Vilcea": ["Craiova", "Pitesti", "Sibiu"],
    "Sibiu": ["Arad", "Rimnicu Vilcea", "Fagaras", "Oardea"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"]
}

def bfs_connected_component(graph, start):
    visted = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visted:
            visted.append(node)
            queue = queue + graph[node]

    
    return visted


def dfs_connected_component(graph, start):
    visted = []
    stack = [start]
    
    while stack:
        node = stack.pop(0)
        
        if node not in visted:
            visted.append(node)
            stack = graph[node] + stack
    
    return visted
    
    
    
def bfs_search(graph, start, end):
    visted = []
    queue = [start]
    parent = {start: None}
    
    while queue:
        node = queue.pop(0)
        # print(node)
        
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        
        visted.append(node)
        for neighbor in graph[node]:
            if neighbor not in queue and neighbor not in visted:
                queue.append(neighbor)
                parent[neighbor] = node
                    

def dfs_search(graph, start, end):
    visted = []
    stack = [start]
    parent = {start: None}
    
    while stack:
        node = stack.pop(0)
        
        if node == end:
            path = []
            
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        visted.append(node)
        for neighbour in graph[node]:
            if neighbour not in visted and neighbour not in stack:
                stack.insert(0, neighbour)
                parent[neighbour] = node
                


# print(bfs_connected_component(graph, "Zerind"))
# print(dfs_connected_component(graph, "Zerind"))
print(dfs_search(graph, "Zerind", "Bucharest"))
print(bfs_search(graph, "Zerind", "Bucharest"))
