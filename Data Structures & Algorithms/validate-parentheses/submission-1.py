class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid={"}":"{",")":"(","]":"["}

        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1]!= valid[c]:
                    return False
                stack.pop()
        return len(stack)==0   