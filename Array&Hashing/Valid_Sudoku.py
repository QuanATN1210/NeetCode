from typing import List
class Solution:
    def checkRow(self,row: List[str])-> bool:
        check =[True]*9
        for i in range(len(row)):
            if row[i] == '.':
                continue
            if check[int(row[i])-1] == True:
                check[int(row[i])-1] = False
                continue
            if check[int(row[i])-1] == False:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        matrix =[[]for _ in range(len(board))]
        index =0
        colum =[[board[i][j] for i in range(9)]for j in range(9)]
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                matrix[index].extend(board[i][j:j+3])
                matrix[index].extend(board[i+1][j:j+3])
                matrix[index].extend(board[i+2][j:j+3])
                index+=1
        result=True
        for i in range(len(board)):
            result = self.checkRow(board[i])
            if result == False:
                return False
        for i in range(len(colum)):
            result = self.checkRow(colum[i])
            if result == False:
                return False
        for i in range(len(matrix)):
            result = self.checkRow(matrix[i])
            if result == False:
                return False
        return True
'''
Time complexity O(n^2)
Space complexity O(n^2)
'''




        