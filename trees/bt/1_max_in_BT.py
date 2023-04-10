
import queue
import sys

class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

################################

def createBT():

	n = int(input("Enter number of elements in tree:"))

	root = Node(int(input("Enter root data: ")))

	q = queue.Queue()

	q.put(root)
	
	while(q.empty() != True):

		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data)+" : "))

		if(left_data != -1):
			node.left = Node(left_data)
			q.put(node.left)
		
		right_data = int(input("Enter right data of "+str(node.data)+" : "))
		
		if(right_data != -1):
			node.right = Node(right_data)
			q.put(node.right)

	
	return root

###############################

def printLevelWiseBT(root):

	if(root == None):
		return

	q = queue.Queue()
	q.put(root)

	while(q.empty() != True):
		node = q.get()

		print(str(node.data) + ":",end = "")
		if(node.left != None):
			print("L "+str(node.left.data),end = " ")
			q.put(node.left)

		if(node.right != None):
			print("R "+str(node.right.data),end = "")
			q.put(node.right)
	
		print()

#################################

def max_in_BT(root):

	if(root == None):
		return (-sys.maxsize - 1)

	left_max = max_in_BT(root.left)
	right_max = max_in_BT(root.right)

	val = max(left_max,right_max,root.data)

	return val	

################################

root = createBT()
printLevelWiseBT(root)

val = max_in_BT(root)
print(val)
