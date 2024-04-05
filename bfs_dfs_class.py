class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        
        

graph = {
    'A': Node('A', None, ['B', 'E', 'C'], None),
    'B': Node ('B', None, ['D', 'E', 'A'], None),
    'C': Node ('C', None, ['A', 'F', 'G'], None),
    'D': Node('D', None, ['B', 'E'], None),
    'E': Node ('E', None, ['A', 'B', 'D'], None),
    'F': Node ('F', None, ['C'], None),
    'G': Node ('G', None, ['C'], None)
}

def bfs_search(graph, start , end):
    visted = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = graph[node].parent
            return path[::-1]
        
        
        visted.append(node)
        for neighbor in graph[node].actions:
            if neighbor not in queue and neighbor not in visted:
                graph[neighbor].parent = node
                # if neighbor == end:
                #     return actionSequence(graph, end)
                queue.append(neighbor)


def dfs_search(graph, start , end):
    visted = []
    stack = [start]
    
    while stack:
        node = stack.pop(0)
        
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = graph[node].parent
            return path[::-1]
        
        
        visted.append(node)
        for neighbor in graph[node].actions:
            if neighbor not in stack and neighbor not in visted:
                graph[neighbor].parent = node
                # if neighbor == end:
                #     return actionSequence(graph, end)
                stack.insert(0,neighbor)



# def actionSequence(graph, node):
#     path = []
#     while node is not None:
#         path.append(node)
#         node = graph[node].parent
        
#     return path[::-1]


print(bfs_search(graph, 'A', 'D'))
print(dfs_search(graph, 'A', 'D'))