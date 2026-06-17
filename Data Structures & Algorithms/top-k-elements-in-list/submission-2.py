class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq={}
        # for n in nums:
        #     freq[n]= freq.get(n,0)+1
        # sorted_arr=sorted(freq, key=lambda x:freq[x], reverse=True)
        # return sorted_arr[:k] # O(n log n)

        freq={} # O(n)
        for n in nums:
            freq[n]=freq.get(n,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for i,f in freq.items():
            buckets[f].append(i)
        result=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result


        