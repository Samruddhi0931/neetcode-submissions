class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,r=j+1,n-1
                while l<r:
                    total= nums[i]+nums[j]+nums[l]+nums[r]

                    if total < target:
                        l=l+1
                    elif total >target:
                        r=r-1
                    else:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        l=l+1
                        r=r-1
                        while l<r and nums[l]==nums[l-1]:
                            l=l+1
        return result
