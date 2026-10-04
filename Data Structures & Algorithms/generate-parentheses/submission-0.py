class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open, close, cur):
            nonlocal res, n
            if open + close == n * 2:
                res.append(cur)
                return
            
            if open < n:
                backtrack(open + 1, close, cur + "(")
            
            if open > close: 
                backtrack(open, close + 1, cur + ")")
        
        backtrack(0, 0, "")
        return res
