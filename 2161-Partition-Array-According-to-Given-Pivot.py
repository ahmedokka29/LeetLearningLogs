class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s = list()
        e = list()
        b = list()
        for i in range(len(nums)):
            if nums[i]<pivot:
                s.append(nums[i])
            elif nums[i]==pivot:
                e.append(nums[i])
            else:
                b.append(nums[i])
        return s+e+b