class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k: return True
        if len(s) <  k: return False 

        # freq = dict()
        # for i in s:
        #     if i in freq.keys():
        #         freq[i]+=1
        #     else:
        #         freq[i]=1

        # freq = Counter(s)
        # odd = 0
        # for i in freq.keys():
        #     if freq[i]%2 != 0:
        #         odd+=1

        odd = 0
        for i in set(s):
            if s.count(i) % 2 != 0:
                odd+=1
        if(odd<=k):
            return True
        else:
            return False











