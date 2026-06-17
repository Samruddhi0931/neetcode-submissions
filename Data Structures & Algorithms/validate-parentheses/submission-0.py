class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        classs={")":"(","]":"[","}":"{"}

        for c in s:
            if c in classs.values():
                stack.append(c)
            elif c in classs:
                if stack and stack[-1] == classs[c]:
                    stack.pop()
                else:
                    return False
        return not stack




        