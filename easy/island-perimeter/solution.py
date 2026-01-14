class Solution:
  def bfs(self, matrix, visited,  row, col):
    if not matrix:
      return 0
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
      return 1
    if visited[row][col]:
      return 0
    if matrix[row][col] == 0:
      return 1
    visited[row][col] = True
    edgeCount = 0
    edgeCount += self.bfs(matrix, visited, row + 1, col)
    edgeCount += self.bfs(matrix, visited, row - 1, col)
    edgeCount += self.bfs(matrix, visited, row, col + 1)
    edgeCount += self.bfs(matrix, visited, row, col - 1)
    
    return edgeCount

  def findIslandPerimeter(self, matrix):
    # TODO: Write your code here
    row = len(matrix)
    col = len(matrix[0])
    visited = [[False for c in range(col)]for r in range(row)]
    for r in range(row):
      for c in range(col):
        if matrix[r][c] == 1 and not visited[r][c]:
          return self.bfs(matrix, visited, r, c)
    return 0

def assert_test(got, expected):
  print("Result :", got, " Expected: ", expected)
  assert got == expected
  assert type(got) is type(expected)

if __name__ == "__main__":
    sol = Solution()
    assert_test(sol.findIslandPerimeter([[1, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 1, 0, 0],
                            [0, 0, 0, 0, 0]]), 14)

    assert_test(sol.findIslandPerimeter([[0, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 1, 0, 0],
                            [0, 1, 1, 0],
                            [0, 1, 0, 0]]), 12)


    print("\033[92m[OK]\033[0m All test cases passed")
