class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        reverse= str_int[::-1]
        if x >= 0:
            if int(reverse)==x:
                return True
        else:
            return False