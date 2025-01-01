class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if i == 0:
                continue
            left = s[:i]
            right = s[i:]
            ans = max(ans,left.count('0') + right.count('1'))
        return ans
