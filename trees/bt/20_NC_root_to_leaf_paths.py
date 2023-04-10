
import queue

class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

#################################

def createBT():

	n = int(input("Enter size of tree: "))
	
	root = Node(int(input("Enter root data : ")))
	q = queue.Queue()

	q.put(root)
	i = 1

	while(q.empty() != True and i < n):

		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data) +" : "))
		if(left_data != -1):
			node.left = Node(left_data)
			i += 1
			q.put(node.left)

		if(i >= n):
			break

		right_data = int(input("Enter right data of "+str(node.data)+" : "))
		if(right_data != -1):
			node.right = Node(right_data)
			i += 1
			q.put(node.right)

	return root

##################################

def preOrder(root):
	if(root != None):
		print(root.data,end = " ")
		preOrder(root.left)
		preOrder(root.right)

#################################

def print_path(q):
	while(q.empty() != True):
		print(q.get().data,end = " ")
	print()

	########################

def all_paths(root,q):
	if(root == None):
		return 
		
	q.put(root)

	if(root.left == None and root.right == None):
		print_path(q)
		return
	
	all_paths(root.left,q)
	all_paths(root.right,q)

#################################

root = createBT()
preOrder(root)
print()
q = queue.Queue()
all_paths(root,q)
