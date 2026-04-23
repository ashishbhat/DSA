import heapq

# init weights of all nodes to inf
# push all neighbors of start into the heap
# while unvisited nodes remain:
#   - pop the cheapest edge (U,V) from heap
#   - if V is already in MST, skip (stale entry)
#   - add edge (U,V) to MST, mark V as visited
#   - for each neighbor W of V, if a cheaper path is found, push (w, (V,W)) into heap
def prims(g: dict,start: str) -> list:
    pipeline = []
    mst = []
    remaining = set(g.keys())
    weights = {i: float('inf') for i in g.keys()}

    for v, w in g[start]:
        if weights[v] > w:
            weights[v] = w
            heapq.heappush(pipeline,(w,(start,v)))

    remaining.remove(start)

    while remaining:
        _,edge = heapq.heappop(pipeline)
        if edge[1] not in remaining:
            continue
        mst.append(edge)

        remaining.remove(edge[1])
        for v,w in g[edge[1]]:
            if weights[v] > w:
                weights[v] = w
                heapq.heappush(pipeline,(w,(edge[1],v)))

    return mst
        

        



g = {
    'a': [('b', 1), ('c', 3)],
    'b': [('c', 1), ('d', 2), ('e', 1)],
    'c': [('d', 1)],
    'd': [('e', 4)],
    'e': []
}

g = {
    'a': [('b', 1), ('c', 3)],
    'b': [('d', 2), ('c',1),('d',1)],
    'c': [('d', 4),('d',0.5)],
    'd': []
}

g = {                                                                                                                                                                                                                                       
      'a': [('b', 1), ('c', 3)],
      'b': [('c', 2)],                                                                                                                                                                                                                        
      'c': [('d', 10)],
      'd': []
  }
print(prims(g, 'a'))