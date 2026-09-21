class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        n = len(heights)
        for j in range(n + 1):
            while s and (j == n or heights[s[-1]] >= heights[j]):
                i = s.pop()
                area = heights[i] * (j if not s else j - s[-1] - 1)
                max_area = max(max_area, area)
            s.append(j)
        return max_area

