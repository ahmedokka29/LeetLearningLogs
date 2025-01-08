class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # ans = []
        # for l in s:
        #     if l.isalnum():
        #         ans.append(l)
        # 
        # ans = ''.join(ans)
        
        # if len(ans)==0:return True
        
        # s = 0
        # e = len(ans)-1
        # while s<=e:
        #     if ans[s]!=ans[e]:
        #         return False
        #     s+=1    
        #     e-=1
        # return True
        
        ans = ''.join(l for l in s.lower() if l.isalnum())
        
        return ans == ans[::-1]
