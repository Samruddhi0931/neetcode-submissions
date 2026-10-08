class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash={}
        for i in s:
            hash[i]=hash.get(i,0)+1
        for i in range(len(s)):
            if hash[s[i]]==1:
                return i
        return -1

        