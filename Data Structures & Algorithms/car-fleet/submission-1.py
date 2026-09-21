class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted([(position[i], speed[i]) for i in range(n)], reverse=True)

        stack = []
        for p, s in cars:
            dist = target - p
            seconds = dist / s

            if stack and seconds <= stack[-1]:
               continue 

            stack.append(seconds)

        return len(stack)        

