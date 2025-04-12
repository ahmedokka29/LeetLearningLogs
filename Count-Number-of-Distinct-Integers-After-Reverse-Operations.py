class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in nums:
            t = str(i)
            t = int(t[::-1])
            nums.append(t)
            if len(nums) == (2*n):
                break
        return len(set(nums))