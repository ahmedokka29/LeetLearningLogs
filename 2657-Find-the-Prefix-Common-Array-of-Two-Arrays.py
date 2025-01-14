class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # repeated = []
        # c = []
        # for i in range(len(A)):
        #     repeated.append(A[i])
        #     repeated.append(B[i])
        #     c.append(len(repeated)- len(set(repeated)))
        # return c        
        c = []
        s = set()
        for i in range(len(A)):
            s.add(A[i])
            s.add(B[i])
            c.append((2*(i+1))-len(s))
        return c