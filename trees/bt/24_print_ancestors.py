
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

def print_ancestor(root,val):
	
	if(root == None):
		return -1	

	if(root.data == val):
		print(root.data,end = " ")
		return 1

	left = print_ancestor(root.left,val)
	right = print_ancestor(root.right,val)

	if(left == 1 or right == 1):
		print(root.data,end = " ")
		return 1
	else:
		return 0

####################################

def printAllancestors(root,val):
	if(root != None):
		return 0

	if(root.left.data == val or root.right.data == val or printAllancestors(root.left,val) or printAllancestors(root.right,val)):
		print(root.data,end = " ")
		return 1

	return 0

##################################

root = createBT()
printBT(root)

val = int(input("Enter val : "))
val1 = print_ancestor(root,val)
#print("\n\n")
#val1 = printAllancestors(root,val)
