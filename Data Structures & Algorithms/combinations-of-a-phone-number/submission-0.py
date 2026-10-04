class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
            "0": "", "1": ""
        }

        res = [[]]
        for digit in digits:
            new_res = []
            for p in res:
                for letter in phone[digit]:
                    c = p.copy()
                    c.append(letter)
                    new_res.append(c)
            res = new_res
        return ["".join(p) for p in res]  
