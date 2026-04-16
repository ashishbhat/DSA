import heapq
'''
My understand and Pseudocode for Dikistra:
dist[start] = 0
dist[all other nodes] = ∞
 - Put the start into heap
 - while heap not empty:
         - extract the min element U
         - if U is already processed:
                continue;
         - mark U = processed
         - for V in neighbours of U :
                if dist[V] > dist[U] + Edge(U,V):
                   dist[V] = dist[U] + Edge(U,V)
                   heap.push(dist[V], V)
'''

def shortest_path(g: dict, start: str) -> dict:
    dist = {node: float('inf') for node in g}
    dist[start] = 0
    heap = [(0, start)]
    processed = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in processed:
            continue
        processed.add(u)
        for v, weight in g[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(, (dist[v], v))

    return dist

g = {
    'a': [('b', 1), ('c', 3)],
    'b': [('c', 1), ('d', 2), ('e', 1)],
    'c': [('d', 1)],
    'd': [('e', 4)],
    'e': []
}
print(shortest_path(g, 'a'))
