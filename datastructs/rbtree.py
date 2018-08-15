#
#Ritwik Dixit
#Implementation of Red-Black Tree

class RBTreeNode:
	def __init__(self, value,left=None,right=None,color):
		self.value=value
		self.left=left
		self.right=right
		self.color=color