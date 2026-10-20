class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        min_num, max_num = min(hand), max(hand)

        for num in range(min_num, max_num + 1):
            count = counts[num]

            for next_num in range(num, num + groupSize):
                next_count = counts[next_num]
                if next_count < count:
                    return False
                
                counts[next_num] -= count
        
        return True
