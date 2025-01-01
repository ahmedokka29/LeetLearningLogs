class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # for x in range(1, len(nums) + 1):
        #     c = 0
        #     for i in nums:
        #         if i >= x:
        #             c += 1
        #     if c == x:
        #         return x
        # return -1

        nums.sort()
        N = len(nums)
        for x in range(1, N + 1):
            low = 0
            high = N-1
            index = len(nums)
            while low<=high:
                mid = (high + low) // 2
                if nums[mid]>=x:
                    index = mid
                    high = mid - 1
                else:
                    low = mid+1 
            if N - index == x:
                return x



        return -1