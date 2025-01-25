class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for c in range(len(s)-1):
            char1 = ord(s[c])
            char2 = ord(s[c+1])
            ans += abs(char2 - char1)
        return ans