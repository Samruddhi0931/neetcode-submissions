class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        result=list(enumerate(nums))
        result.sort(key=lambda x:x[1])
        start=0
        end=len(nums)-1
        while start<end:
            curr_sum=result[start][1]+result[end][1]
            if curr_sum==target:
                i,j=result[start][0],result[end][0]
                return sorted([i,j])
            elif curr_sum < target:
                start+=1
            else:
                end-=1