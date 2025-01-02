def parity(n1:int,n2:int):
    if ((n1%2) == 0) and ((n2%2) == 0) or  ((n1%2) != 0) and ((n2%2) != 0):
        print(n1)
        print(n2)
        return True
    else:
        return False
class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = list(s)
        for i in range(0,len(ans)-1):
            if parity(int(ans[i]),int(ans[i+1])) and (ans[i] > ans[i+1]):
                ans[i],ans[i+1] = ans[i+1],ans[i]
                break
        return ''.join(ans)
            

    

        