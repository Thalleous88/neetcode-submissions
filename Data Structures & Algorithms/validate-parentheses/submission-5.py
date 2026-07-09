class Solution:
    def isValid(self, s: str) -> bool:
       

        stack = []
        for i in s:
            if stack and ((stack[-1] == "(" and i == ")") or (stack[-1] == "[" and i == "]") or (stack[-1] == "{" and i == "}")):
                stack.pop()
            else:
                stack.append(i)
        
        if stack:
            return False
        
        return True
        