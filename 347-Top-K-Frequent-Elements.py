class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea: return k (number) the most frequent elements 
        # edge cases:
        # approach:
        # frequency array
        # max(element)
        # pop(max(element))
        # repeat last 2 steps k times
        freq = Counter(nums)
        ans = freq.most_common(k)
        r = []
        for i in ans:
            r.append(i[0])
        return r
            
