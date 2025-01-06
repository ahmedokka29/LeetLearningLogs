class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Idea: transfer all balls to box i for each operation
        # edge case: if one element return ans = [0] 
        # sudo:
        # initialize array ans of length n
        # loop over boxes with holding the index i  
        # loop over boxes again with new index
        # compare the index i, j 
        # count operations between i , j
        # add the count to index i in ans array
        n = len(boxes)
        if n == 1:
            return [0]

        ans = [0] * n

        left_balls = 0
        left_ops = 0
        for i in range(n):
            ans[i] += left_ops
            if boxes[i] == '1':
                left_balls += 1
            left_ops += left_balls

        # 110
        # i = 0
        # ans[0] = 0
        # left_balls = 1
        # leftops = 1
        
        # i = 1
        # ans[1] = 1
        # left_balls = 2
        # left_ops = 3

        # i = 2
        # ans[2] = 3
        # left_balls = 2
        # left_ops = 5
        
        right_balls = 0
        right_ops = 0
        for i in range(n-1, -1, -1):
            ans[i] += right_ops
            if boxes[i] == '1':
                right_balls += 1
            right_ops += right_balls
        print(right_balls)
        print(right_ops)        
        # 110
        # i = 2
        # ans[2] = 3
        # right_balls = 0
        # right_ops = 0
        
        # i = 1
        # ans[1] = 1
        # right_balls = 1
        # right_ops = 1

        # i = 0
        # ans[0] = 1
        # right_balls = 2
        # right_ops = 3

        return ans