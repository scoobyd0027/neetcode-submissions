class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == '+':
                res = s.pop() + s.pop()
            elif token == '-':
                last = s.pop()
                res = s.pop() - last
            elif token == '*':
                 res = s.pop() * s.pop()
            elif token == '/':
                last = s.pop()
                res = int(float(s.pop()) / last)
            else:
                res = int(token)
            s.append(res)
        
        return s.pop()

            