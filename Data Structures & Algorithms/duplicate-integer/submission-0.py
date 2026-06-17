class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list=[]
        count=0
        for a in nums:
            if a in list:
              return True
            list.append(a)
        return False
       
        