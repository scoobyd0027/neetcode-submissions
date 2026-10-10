class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = Counter()
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            indegrees[b] += 1
            prereqs[a].append(b)

        q = deque() # a, f, e, g
        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)
    
        take = 0
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            take += 1
            for next in prereqs[course]:
                indegrees[next] -= 1
                if indegrees[next] == 0:
                    q.append(next)
        return order[::-1] if take == numCourses else []