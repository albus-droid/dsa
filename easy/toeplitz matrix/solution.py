class Solution:
    def isToeplitzMatrix(self, matrix):
        #  ToDo: Write Your Code Here.
        for i in range(len(matrix) - 1): # ignore  the last row
            for j in range(len(matrix[0])- 1): # ignore the last column
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
