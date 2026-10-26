class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx, ty, tz = target
        max_x, max_y, max_z = 0, 0, 0
        for x, y, z in triplets:
            if x > tx or y > ty or z > tz:
                continue
            
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            max_z = max(max_z, z)

        return max_x == tx and max_y == ty and max_z == tz
            
