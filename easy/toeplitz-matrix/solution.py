class Solution:
    def isToeplitzMatrix(self, matrix):
        #  ToDo: Write Your Code Here.
        for i in range(len(matrix) - 1): # ignore  the last row
            for j in range(len(matrix[0])- 1): # ignore the last column
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

# Testing the algorithm with example inputs
if __name__ == "__main__":
    solution = Solution()
    print(solution.isToeplitzMatrix([[1, 2, 3], [4, 1, 2], [5, 4, 1]]))  # true
    print(solution.isToeplitzMatrix([[1, 2], [3, 4]]))  # false
    print(solution.isToeplitzMatrix([[7, 7, 7], [7, 7, 7], [7, 7, 7]]))  # true
