class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        c = 0
        
        for i in range(n):
            for j in range(i,n):
                q = nums[:i] + nums[j + 1:]
                if (q == sorted(q)) and (len(set(q)) == len(q)):
                    c+=1
                # print(nums[i:j+1]," ",nums[0:j]," ",nums[j+1:])
        return c