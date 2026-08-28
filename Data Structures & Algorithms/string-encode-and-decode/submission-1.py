class Solution:
    seperator = "@s@"
    empty = "@empty@"

    def encode(self, strs: List[str]) -> str:
        return self.seperator.join(strs) if strs else self.empty

    def decode(self, s: str) -> List[str]:
        return s.split(self.seperator) if s != self.empty else []
