class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))
        # for i in range(len(s)):
        #     if s[i]!=t[i]:
        #         return t[i]
        # return t[-1]
        
        freq = Counter(t)
        freq_s = Counter(s)
        return list((freq - freq_s).keys())[0]