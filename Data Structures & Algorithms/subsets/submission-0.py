class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start):
            result.append(current[:])          # record a COPY of the current subset at every step
                                              # (not just at the "end" -- every partial state IS a valid subset!)

            for i in range(start, len(nums)):
                current.append(nums[i])           # CHOOSE: include nums[i]
                backtrack(i + 1)                    # EXPLORE: recurse using only elements after i
                current.pop()                        # UNDO: remove nums[i] before trying the next option

        backtrack(0)
        return result