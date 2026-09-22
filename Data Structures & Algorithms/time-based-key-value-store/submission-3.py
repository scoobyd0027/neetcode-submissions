from collections import defaultdict
from bisect import bisect_left

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.map[key]: return ""
        i = bisect_left(self.map[key], (timestamp,))
        return self.map[key][i][1] if i < len(self.map[key]) and self.map[key][i][0] == timestamp else self.map[key][i - 1][1] if i != 0 else ""

'''
(10, "one"), (20, "two"), (30, "three")

(1, "happy"), (2, "alice"), (3, "sad")
'''