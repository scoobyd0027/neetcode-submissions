from collections import Counter

class UF:
    def __init__(self):
        self.parent = {}
        self.size = Counter()
    
    def find(self, node):
        if node in self.parent and node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node] if node in self.parent else node
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.size[pv] > self.size[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF()
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        
        return []