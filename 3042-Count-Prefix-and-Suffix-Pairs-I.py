def isPrefixAndSuffix(str1,str2):
    if str2.startswith(str1) and str2.endswith(str1):
        return True

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = 0
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    # print(f"words[{i}] : {words[i]}   words[{j}] : {words[j]}")
                    c+=1
        
        return c

        