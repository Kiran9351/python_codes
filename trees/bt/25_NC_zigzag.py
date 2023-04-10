
import queue

class Node:
	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

##################################

def createBT():

	n = int(input("Enter no. of nodes : "))
	
	root = Node(int(input("Enter the root data: ")))

	q = queue.Queue()

	q.put(root)

	i = 1

	while(q.empty() != True and i< n):
		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data)+" : "))
		if(left_data != -1):
			node.left = Node(left_data)
			q.put(node.left)
			i += 1

		if(i == n):
			break

		right_data = int(input("Enter right data of "+str(node.data)+" : "))
		if(right_data != -1):
			node.right = Node(right_data)
			q.put(node.right)
			i += 1

	return root

###################################

def printBT(root):
	
	if(root == None):
		return 

	q = queue.Queue()

	q.put(root)

	while(q.empty() != True):
		node = q.get()

		print(node.data,end = " : ")
		if(node.left != None):
			print("L "+str(node.left.data),end = " ")
			q.put(node.left)
		
		if(node.right != None):
			print("R "+str(node.right.data))
			q.put(node.right)

		print()

####################################

def zigzag(root):
	
	if(root == None):
		return None

	flag = 0

	q = queue.Queue()

	q.put(root)

	while(q.empty() != True):

		node = q.get())
		
		if(node.left != None):
			q.put(node.left)
	
		if(node.right != None):
			q.put(node.right)

		

	print()

######################################

root = createBT()
printBT(root)
zigzag(root)
