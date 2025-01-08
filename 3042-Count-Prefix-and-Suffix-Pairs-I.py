def isPrefixAndSuffix(str1,str2):
    if str2.startswith(str1) and str2.endswith(str1):
        return True

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = 0
        n = len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                if isPrefixAndSuffix(words[i],words[j]):
                    # print(f"words[{i}] : {words[i]}   words[{j}] : {words[j]}")
                    c+=1
        
        return c

        