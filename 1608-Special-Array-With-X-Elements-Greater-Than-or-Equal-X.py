class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(1,len(nums)+1):
            c = 0
            for i in nums:
                if i >= x:
                    c+=1
            if c == x: 
                return x
        return -1 




        