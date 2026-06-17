class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list=[]
        count=0
        for i in nums:
            if i in list:
                return True
            else:
                list.append(i)
                print(i)
        return False
       
        '''
        U - Understand
            I-nums array
            O- false/true
            C- not given
            E- empty array
        P- Plan
            take an input array 
            take a counter
            if counter>1 then flag true, else false
        '''