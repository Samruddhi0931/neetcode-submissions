class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash={}
        for i in s:
            hash[i]=hash.get(i,0)+1
        length=0
        has_odd=False

        for i,ch in hash.items():
            length+=(ch//2)*2

            if ch %2 ==1:
                has_odd=True
        if has_odd:
            length+=1
        return length
        