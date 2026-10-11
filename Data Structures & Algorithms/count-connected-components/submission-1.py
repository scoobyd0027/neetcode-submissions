from collections import Counter

class UF:
    def __init__(self, n):
        self.comp = n
        self.parent = list(range(n))
        self.size = Counter()
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        self.comp -= 1
        if self.size[pv] > self.size[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.comp
