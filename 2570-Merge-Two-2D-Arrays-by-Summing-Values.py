class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d1 = dict(nums1)
        d2 = dict(nums2)
        both = Counter(d1)+Counter(d2)
        both = sorted(both.items())
        ans = list(both)

        return ans