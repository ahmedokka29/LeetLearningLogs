class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        row = 9
        
        for x in range(row):
            numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for y in range(row):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        return False 

        for y in range(row):
            numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for x in range(row):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        return False 

        # for r in range(0,9,3):
        #     for c in range(0,9,3):        
        #         numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        #         for x in range(0+r,3+r):
        #             for y in range(0+c,3+c):
        #                 if board[x][y] in numbers.keys():
        #                     numbers[board[x][y]] += 1
        #                     if numbers[board[x][y]] > 1:
        #                         return False 
            
        for c in range(0,9,3):        
            numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for x in range(0,3):
                for y in range(0+c,3+c):
                    if board[x][y] in numbers.keys():
                        numbers[board[x][y]] += 1
                        if numbers[board[x][y]] > 1:
                            return False 

        for c in range(0,9,3):        
            numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for x in range(3,6):
                for y in range(0+c,3+c):
                    if board[x][y] in numbers.keys():
                        numbers[board[x][y]] += 1
                        if numbers[board[x][y]] > 1:
                            return False 

        for c in range(0,9,3):        
            numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for x in range(6,9):
                for y in range(0+c,3+c):
                    if board[x][y] in numbers.keys():
                        numbers[board[x][y]] += 1
                        if numbers[board[x][y]] > 1:
                            return False 
        
        return True

