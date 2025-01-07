class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for  j in words:
                if (j in i) and (len(i)!=len(j)):
                    if j not in ans:
                        ans.append(j)
        return ans
        

