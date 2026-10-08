class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash1={}
        hash2={}
        for i in ransomNote:
            hash1[i]=hash1.get(i,0)+1
        for i in magazine:
            hash2[i]=hash2.get(i,0)+1
        for i in ransomNote:
            if hash1[i]>hash2.get(i,0):
                return False
        return True

        