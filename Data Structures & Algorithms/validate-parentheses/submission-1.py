class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        for i in s:
            if stack and ((stack[-1] == "(" and i == ")") or (stack[-1] == "[" and i == "]") or (stack[-1] == "{" and i == "}")):
                stack.pop(-1)
            else:
                stack.append(i)
        print(stack)
        if len(stack) > 0:
            return False
        
        return True
        