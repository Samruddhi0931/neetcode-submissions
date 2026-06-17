class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,value in enumerate(nums):
            need=target-value

            if need in seen:
                return [seen[need],i]
            seen[value]=i



        