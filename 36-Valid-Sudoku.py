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
                        print('fuck rows')
                        return False 

        for y in range(row):
            numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
            for x in range(row):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck col')
                        return False 

        # for i in range(3,row,3):

        #     for x in range(i):
        #         numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        #         for y in range(i):
        #             print('x',x,'y',y)
        #             # print(board[x][y])
        #             if board[x][y] in numbers.keys():
        #                 numbers[board[x][y]] += 1
        #                 if numbers[board[x][y]] > 1:
        #                     print('fuck boxes')
        #                     return False 
        #             # print(numbers)
        # for i in range(2):
        #     for x in range(i):
        #         for y in range(x):
        #             print(board[x][y])

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(0,3):
            for y in range(0,3):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 1')
                        return False 

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(0,3):
            for y in range(3,6):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 2')
                        return False

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(0,3):
            for y in range(6,9):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 3')
                        return False 

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(3,6):
            for y in range(0,3):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 4')
                        return False 

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(3,6):
            for y in range(3,6):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 5')
                        return False 

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(3,6):
            for y in range(6,9):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 6')
                        return False 

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(6,9):
            for y in range(0,3):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 7')
                        return False 

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(6,9):
            for y in range(3,6):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 8')
                        return False 

        numbers = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        for x in range(6,9):
            for y in range(6,9):
                if board[x][y] in numbers.keys():
                    numbers[board[x][y]] += 1
                    if numbers[board[x][y]] > 1:
                        print('fuck boxes 9')
                        return False 
        
        return True

