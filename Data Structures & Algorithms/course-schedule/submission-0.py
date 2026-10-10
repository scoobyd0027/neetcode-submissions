from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        next_courses = defaultdict(list)
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            next_courses[b].append(a)
            prereqs[a].append(b)

        taken = [False] * numCourses
        q = deque() # a, f, e, g
        for course in range(numCourses):
            if course not in prereqs:
                taken[course] = True
                q.append(course)

        def all_prereqs_done(course):
            for prereq in prereqs[course]:
                if not taken[prereq]:
                    return False
            return True

        take = 0
        while q:
            course = q.popleft()
            take += 1
            for next in next_courses[course]:
                if not taken[next] and all_prereqs_done(next):
                    taken[next] = True
                    q.append(next)
        return take == numCourses

'''
       f 
        \
a -> b -> c -> d
    /     /  
   e     g
'''
