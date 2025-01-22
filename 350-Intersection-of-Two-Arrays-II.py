class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # This Solution return wrong answer on test case 40
        # ans = list()
        # l_1 = len(nums1)
        # l_2 = len(nums2)
        # if l_1>l_2:
        #     for i in nums1:
        #         if i in nums2 and i not in ans:
        #             ans.append(i)
        # else:
        #     for i in nums2:
        #         if i in nums1 and i not in ans:
        #             ans.append(i)
        # return ans

        f_1 = Counter(nums1)
        f_2 = Counter(nums2)
        ans = list()
        for i in f_1.keys():
            if i in f_2.keys():
                k = min(f_1[i], f_2[i])
                for j in range(k):
                    ans.append(i)
        return ans
