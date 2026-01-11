from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

class Solution:
  def findDepth(self, root):
    
    minimumTreeDepth = 0
    
    if not root:
      return 0
    
    if not root.left:
      return 1 + self.findDepth(root.right)
    
    if not root.right:
      return 1 + self.findDepth(root.left)
    
    LDepth = self.findDepth(root.left)
    RDepth = self.findDepth(root.right)
    
    minimumTreeDepth = min(LDepth, RDepth) + 1

    return minimumTreeDepth

def assert_test(got, expected):
  print("Result :", got, " Expected: ", expected)
  assert got == expected
  assert type(got) is type(expected)

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  assert_test(sol.findDepth(root), 2)
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  assert_test(sol.findDepth(root), 3)

  print("\033[92m[OK]\033[0m All test cases passed")

if __name__ == "__main__":
	main()
