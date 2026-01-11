class Solution:
    def isToeplitzMatrix(self, matrix):
        #  ToDo: Write Your Code Here.
        for i in range(len(matrix) - 1): # ignore  the last row
            for j in range(len(matrix[0])- 1): # ignore the last column
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

# Testing the algorithm with example inputs
def assert_test(got, expected):
	print("Result :", got, " Expected: ", expected)
	assert got == expected
	assert type(got) is type(expected)
	
if __name__ == "__main__":
    solution = Solution()
    assert_test(solution.isToeplitzMatrix([[1, 2, 3], [4, 1, 2], [5, 4, 1]]), True)  # true
    assert_test(solution.isToeplitzMatrix([[1, 2], [3, 4]]), False)  # false
    assert_test(solution.isToeplitzMatrix([[7, 7, 7], [7, 7, 7], [7, 7, 7]]), True)  # true

    print("\033[92m[OK]\033[0m All test cases passed")

