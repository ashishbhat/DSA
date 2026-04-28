from union_find import UnionFind

def mst(edges: list, vertices: dict) -> list:
    result = []
    uf = UnionFind(vertices)
    target = len(vertices) - 1

    for w, (u, v) in sorted(edges, key=lambda e: e[0]):
        if uf.union(u, v):
            result.append((w, (u, v)))
            if len(result) == target:
                break

    if len(result) != target:
        raise ValueError("graph is disconnected; no spanning tree exists")

    return result

if __name__ == "__main__":
    def total_weight(tree):
        return sum(w for w, _ in tree)

    def vertices(n):
        return {i: [] for i in range(1, n + 1)}

    # 1. Sample from review: 4 vertices, expected MST weight 6
    g1 = vertices(4)
    e1 = [(1,(1,2)),(2,(2,4)),(3,(1,3)),(4,(3,4)),(5,(1,4))]
    t1 = mst(e1, g1)
    assert total_weight(t1) == 6, t1
    assert len(t1) == 3

    # 2. Single vertex: empty MST
    t2 = mst([], vertices(1))
    assert t2 == []

    # 3. Two vertices, one edge
    t3 = mst([(7, (1, 2))], vertices(2))
    assert t3 == [(7, (1, 2))]

    # 4. Cycle of equal-weight edges: any V-1 of them is valid; weight must be V-1
    g4 = vertices(3)
    e4 = [(1,(1,2)),(1,(2,3)),(1,(1,3))]
    t4 = mst(e4, g4)
    assert len(t4) == 2 and total_weight(t4) == 2

    # 5. Parallel edges between same pair: cheaper one wins
    g5 = vertices(3)
    e5 = [(10,(1,2)),(1,(1,2)),(2,(2,3))]
    t5 = mst(e5, g5)
    assert total_weight(t5) == 3, t5

    # 6. Input list must NOT be mutated (we use sorted(), not .sort())
    e6 = [(3,(1,2)),(1,(2,3)),(2,(1,3))]
    snapshot = list(e6)
    mst(e6, vertices(3))
    assert e6 == snapshot, "mst() mutated caller's edge list"

    # 7. Disconnected graph: should raise
    try:
        mst([(1,(1,2))], vertices(4))
    except ValueError:
        pass
    else:
        assert False, "expected ValueError on disconnected graph"

    # 8. Larger graph (CLRS-style): expected MST weight 37
    g8 = vertices(9)
    e8 = [
        (4,(1,2)),(8,(1,8)),
        (8,(2,3)),(11,(2,8)),
        (7,(3,4)),(2,(3,9)),(4,(3,6)),
        (9,(4,5)),(14,(4,6)),
        (10,(5,6)),
        (2,(6,7)),
        (1,(7,8)),(6,(7,9)),
        (7,(8,9)),
    ]
    t8 = mst(e8, g8)
    assert len(t8) == 8
    assert total_weight(t8) == 37, total_weight(t8)

    print("all tests passed")