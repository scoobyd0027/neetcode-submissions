from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        while q:
            course = q.popleft()
            take += 1
            for next in prereqs[course]:
                indegrees[next] -= 1
                if indegrees[next] == 0:
                    q.append(next)
        return take == numCourses

'''
       f 
        \
a -> b -> c -> d
    /     /  
   e     g
'''
