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
            if boxes[i] == "1":
                left_balls += 1
            left_ops += left_balls

        right_balls = 0
        right_ops = 0
        for i in range(n - 1, -1, -1):
            ans[i] += right_ops
            if boxes[i] == "1":
                right_balls += 1
            right_ops += right_balls

        # for i in range(n):
        #     for j in range(n):
        #         if i != j:
        #             if int(boxes[j]) == 1:
        #                 ans[i] += abs(j-i)

        return ans
