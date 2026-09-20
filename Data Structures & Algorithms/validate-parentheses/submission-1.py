class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_brackets = [')', '}', ']']
        for ch in s:
            if stack and ((ch == ')' and stack[-1] == '(') \
            or (ch == '}' and stack[-1] == '{') \
            or (ch == ']' and stack[-1] == '[')):
                stack.pop()
                continue
            
            if ch in closing_brackets:
                return False
            
            stack.append(ch)
        return not stack
