class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2
        m = 0
        # print(nums)
        # while nums:
        #     m = max(nums[0]+nums[-1],m)
        #     nums.pop(0)
        #     nums.pop(-1)
        
        for i in range(n):
            m = max(nums[i]+nums[-i-1],m)
        return m