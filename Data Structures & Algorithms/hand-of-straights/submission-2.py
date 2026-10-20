class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        counts = Counter(hand)
        min_num, max_num = min(hand), max(hand)

        for num in range(min_num, max_num + 1):
            if num not in counts or counts[num] == 0: continue
            count = counts[num]

            for next_num in range(num, num + groupSize):
                next_count = counts[next_num]
                if next_count < count:
                    return False
                counts[next_num] -= count
        
        return True
