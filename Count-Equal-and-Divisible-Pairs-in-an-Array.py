class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = list()
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if (nums[i]==nums[j]) and ((i*j)%k==0):
                    ans.append((nums[i],nums[j]))
        # print(ans)
        return len(ans)

