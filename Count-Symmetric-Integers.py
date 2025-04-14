class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            t = str(i)
            s1=0
            s2=0
            if len(t) %2==0:
                for h in t[:(len(t)//2)]:
                    s1+=int(h)
                for h in t[(len(t)//2):len(t)+1]:
                    s2+=int(h)
                if s1 == s2:
                    count+=1
        return count


