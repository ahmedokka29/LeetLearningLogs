class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:return 0
        
        nums.sort()
        n = len(nums)

        if k == n:return (nums[-1]-nums[0]) 
        
        min_diff = float('inf')
        for i in range(n):
            if (k+i)<=n:
                min_diff = min(min_diff,(nums[k+i-1]-nums[i]))

        return min_diff
