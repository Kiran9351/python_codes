
import queue

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

################################

def createBT():

	n = int(input("Enter number of elements in tree : "))
	i = 0

	rootData = int(input("Enter root data: "))
	root = Node(rootData)
	
	q = queue.Queue()

	q.put(root)
	i += 1
	while((q.empty() != True) and i <= n):
		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data)+" : "))

		if(left_data != -1):
			node.left = Node(left_data)
			q.put(node.left)
			i += 1

		right_data = int(input("Enter right data of "+str(node.data)+" : "))
		
		if(right_data != -1):
			node.right = Node(right_data)
			q.put(node.right)
			i += 1
	
	return root

##############################

def preOrder(root):

	if(root != None):
		print(root.data,end = " ")
		preOrder(root.left)
		preOrder(root.right)

##############################

def printLevelWise(root):

	q = queue.Queue()
	q.put(root)
	
	while(q.empty() != True):
		node = q.get()

		print(node.data,end = ":")
		if(node.left != None):
			print("L "+str(node.left.data),end = " ")
			q.put(node.left)

		if(node.right != None):
			print("R "+str(node.right.data),end = "")
			q.put(node.right)

		print()

##############################

def max_in_BT(root):
	
	q = queue.Queue()

	q.put(root)

	max_data = root.data

	while(q.empty() != True):
		
		node = q.get()


		if(node.data > max_data):
			max_data = node.data

		if(node.left != None):
			q.put(node.left)

		if(node.right != None):
			q.put(node.right)

	return max_data

################################

root = createBT()
printLevelWise(root)
preOrder(root)
print()
val = max_in_BT(root)
print(val)
				
