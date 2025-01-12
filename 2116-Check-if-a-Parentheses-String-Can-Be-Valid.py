class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # idea: make valid parentheses string
        # edge cases: 1. n == odd number return false
        #             2. check valid parentheses at first before anything
        # approch:
        # s =      " ( ) ) ( ) ) )" 
        # locked = " 0 1 0 1 0 0"
        # s l min_open max_open
        # ) 0 -1 0   1
        # ) 1 -2 0   0
        # ( 0 -3 0   1
        # ) 1 -4 0   0
        # ) 1 -5 0   -1
        # ) 0 -6 0   0

        n = len(s)
        if n % 2 != 0:
            return False
        
        if (locked[0] == "1" and s[0] == ")") or (locked[-1] == "1" and s[-1] == "("):
            return False 
        
        min_open = 0
        max_open = 0
        
        for i in range(n):
            if locked[i] == '0':
                # If the character is unlocked, it can be either '(' or ')'
                min_open -= 1
                max_open += 1
            else:
                # If the character is locked, it can only be what it is
                if s[i] == '(':
                    min_open += 1
                    max_open += 1
                else:
                    min_open -= 1
                    max_open -= 1
            
            # If at any point, the maximum number of open parentheses is negative,
            # it means we have more closing parentheses than opening ones, which is invalid
            if max_open < 0:
                return False
            
            # The minimum number of open parentheses cannot be negative
            min_open = max(min_open, 0)
        
        # Finally, check if the minimum number of open parentheses is zero
        return min_open == 0
