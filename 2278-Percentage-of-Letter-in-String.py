class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l_s = len(s)
        l = s.count(letter)
        ans = l / l_s
        return floor((ans*100))
        