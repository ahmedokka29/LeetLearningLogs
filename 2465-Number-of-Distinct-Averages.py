class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # avgs = set()
        # while nums:
        #     avgs.add(((max(nums)+min(nums))/2))
        #     nums.remove(max(nums))
        #     nums.remove(min(nums))

        # return len(avgs)

        avg_s = set()
        nums = sorted(nums)
        s , e = 0,len(nums)-1
        while s<e:
            t = (nums[s]+nums[e])/2
            avg_s.add(t)
            s+=1
            e-=1
        
        return len(avg_s)