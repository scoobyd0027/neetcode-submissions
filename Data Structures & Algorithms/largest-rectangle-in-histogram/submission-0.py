class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        for j, h in enumerate(heights):
            start = j
            while s and s[-1][1] > h:
                i, ph = s.pop()
                area = ph * (j - i)
                max_area = max(max_area, area)
                start = i
            s.append([start, h])

        for i, h in s:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

