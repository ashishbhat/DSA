class UnionFind:
    class Node:
        def __init__(self, val: int) -> None:
            self._val = val
            self._parent = self
            self._rank= 0
    
    def __init__(self, g: dict) -> None:
        self.__elements = []
        self.__elements.insert(0,None)
        for k in g.keys():
            self.__elements.insert(k,UnionFind.Node(k))

    def union(self, u: int, v: int) -> None:
        src_root= self.find(u)
        dst_root = self.find(v)

        if src_root == dst_root:
            return
        
        if src_root._rank == dst_root._rank:
            dst_root._parent = src_root._parent
            src_root._rank += 1
        elif src_root._rank > dst_root._rank:
            dst_root._parent = src_root
        else:
            src_root._parent = dst_root

    def __is_valid_node(self, n) -> bool:
        if n < 1 or n >= len(self.__elements):
            return False
        return True
    
    def is_connected(self, m, n):
        if self.find(m) == self.find(n):
            return True
        else:
            return False
    
    def find(self, m):
        node = self.__elements[m]

        while node._parent._val != node._val:
            node = node._parent
        
        return node

    
    def get_elements(self) -> list:
        return self.__elements



