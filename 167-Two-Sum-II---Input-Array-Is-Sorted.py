class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for i in range(len(numbers)):
        #     c = target - numbers[i]
        #     l = i+1
        #     h = len(numbers)-1
        #     while l<=h:
        #         mid = (h + l) // 2
        #         if numbers[mid] == c:
        #             return [i+1,mid+1]
        #         elif numbers[mid] > c:
        #             l = mid - 1
        #         else:
        #             h = mid + 1
        # return []
        l, r = 0, len(numbers) - 1

        while l <= r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1
