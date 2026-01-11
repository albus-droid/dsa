class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def __init__(self):
    self.treeDiameter = 0;

  def maxDepth(self, node):
    if not node:
      return 0
    
    Ldepth = self.maxDepth(node.left)
    Rdepth = self.maxDepth(node.right)

    diameter = Ldepth + Rdepth + 1
    self.treeDiameter = max(self.treeDiameter, diameter)

    return max(Ldepth, Rdepth) + 1  

  def findDiameter(self, root):
    self.maxDepth(root)
    return self.treeDiameter
