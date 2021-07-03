from math import inf
from queue import PriorityQueue

def dijkstra(G, x, y):
    parent = [None] * len(G)
    value = [inf] * len(G)
    value[x] = 0
    
    V = PriorityQueue()    
    V.put((0, x))
    
    while not V.empty():
        val, t = V.get()
        if val == value[t]:
            for e in G[t]:
                 if value[e[0]] > value[t] + e[1]:
                    value[e[0]] = value[t] + e[1]
                    parent[e[0]] = t 
                    V.put((value[e[0]], e[0]))

    return value[y]

G = [
    [(2, 7), (4, 1)],
    [(4, 4),(3, 5), (5, 6)],
    [(0, 7), (3, 2), (5, 3), (4, 8)],
    [(2, 2), (1, 5)],
    [(0, 1), (1, 4), (5, 12), (3, 8)],
     [(4, 12), (1, 6), (2, 3)],   
]
print(dijkstra(G, 5, 4))
    
    
G = [
    [(1, 1), (2, 5)],
    [(4, 7), (0, 1), (2, 2), (3, 8)],
    [(1, 2), (0, 5), (3, 3)],
    [(2, 3), (1, 8), (4, 1)],
    [(1, 7), (3, 1)]
]
print(dijkstra(G, 0, 4))

def dijkstra_matrix(G, x, y):
    parent = [None] * len(G)
    value = [inf] * len(G)
    value[x] = 0
    
    V = PriorityQueue()    
    V.put((0, x))
    
    while not V.empty():
        val, t = V.get()
        if val == value[t]:
            for e in range(len(G)):
                if G[t][e] > 0:
                 if value[e] > value[t] + G[t][e]:
                    value[e] = value[t] + G[t][e]
                    parent[e] = t 
                    V.put((value[e], e))

    return value[y]

G = [
    [0, 0, 7, 0, 1, 0],  
    [0, 0, 0, 5, 4, 6],  
    [7, 0, 0, 2, 8, 3],  
    [0, 5, 2, 0, 0, 0],  
    [1, 4, 8, 0, 0, 12],  
    [0, 6, 3, 0, 12, 0],  
]
print(dijkstra_matrix(G, 5, 4))
    
    
G = [
    [0, 1, 5, 0, 0],
    [1, 0, 2, 8, 7],
    [5, 2, 0, 3, 0],
    [0, 8, 3, 0, 1],
    [0, 7, 0, 1, 0],
]
print(dijkstra_matrix(G, 0, 4))