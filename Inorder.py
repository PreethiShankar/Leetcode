#Inorder
class TreeNode():
  def __init__(self, value):
     self.left = None
     self.right = None
     self.value = value
  
def printtree(root):
  if root != None:
    printtree(root.left)
    print(root.value)
    printtree(root.right)

if __name__ == '__main__':
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3)
  n1.left = n2
  n1.right = n3
  n1.left.left = TreeNode(4)
  n1.left.right = TreeNode(5)
  n1.right.left = TreeNode(6)
  n1.right.right = TreeNode(7)
  printtree(n1)
