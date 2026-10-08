class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash={}
        for i in text:
            hash[i]=hash.get(i,0)+1
        need={'b':1,'a':1,'l':2,'o':2,'n':1}
        ans=float("inf")
        for ch,k in need.items():
            ans=min(ans,hash.get(ch,0)//k)
        return ans
        