class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for j, temp in enumerate(temperatures):
            while s and temp > temperatures[s[-1]]:
                i = s.pop()
                res[i] = j - i
            s.append(j) 
        
        return res
