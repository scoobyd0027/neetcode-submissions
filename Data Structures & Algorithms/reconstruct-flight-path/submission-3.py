class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for fro, to in tickets:
            graph[fro].append(to)

        res = []
        def dfs(src):
            while graph[src]:
                dfs(graph[src].pop())
            res.append(src)

        dfs('JFK')
        return res[::-1]
