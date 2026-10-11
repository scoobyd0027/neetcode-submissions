from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        count = 0
        vis = [False] * n
        q = [(0, -1)]
        vis[0] = True
        while q:
            node, parent = q.pop()
            count += 1
            for neig in graph[node]:
                if not vis[neig]:
                    vis[neig] = True
                    q.append((neig, node))
                elif neig != parent:
                    return False

        return count == n
        
        