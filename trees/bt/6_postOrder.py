
import queue

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

###############################

def createBT():

	q = queue.Queue()
	n = int(input("enter number of nodes in BT : "))

	root = Node(int(input("Enter root data : ")))

	q.put(root)
	i = 0 
	while(q.empty() != True and i < n):
		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data)+" : "))
		if(left_data != -1):
			node.left = Node(left_data)
			q.put(node.left)
			i += 1
		
		right_data = int(input("Enter right of " + str(node.data) + " : "))
		if(right_data != -1):
			node.right = Node(right_data)
			q.put(node.right)
			i += 1
	
	
	return root

################################

def preOrder(root):

	if(root != None):
		print(str(root.data),end = " ")
		preOrder(root.left)
		preOrder(root.right)

################################

def inOrder(root):
	if(root != None):
		inOrder(root.left)
		print(root.data,end = " ")
		inOrder(root.right)

###############################

def postOrder(root):
	if(root != None):
		postOrder(root.left)
		postOrder(root.right)
		print(root.data,end = " ")

###############################
def printLevelWise(root):
	
	q = queue.Queue()

	q.put(root)

	while(q.empty() != True):
		node = q.get()
		
		print(node.data,end = ":")
		if(node.left != None):
			print("L "+str(node.left.data),end = ", ")
			q.put(node.left)

		if(node.right != None):
			print("R "+str(node.right.data))
			q.put(node.right)
		
		print()

##################################

root = createBT()
printLevelWise(root)
preOrder(root)
print()
inOrder(root)
print()
postOrder(root)
print()
