import queue

class Node:
	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

#################################

def insert_bst(root,data):
	if(root == None):
		root = Node(data)
	elif(root.data < data):
		root.right = insert_bst(root.right,data)
	elif(root.data > data):
		root.left = insert_bst(root.left,data)

	return root

	#########################

def createBst():

	n = int(input("Enter size of bst: "))
	
	i = 0
	root = None

	while(i < n):
		data = int(input("Enter data: "))
		root = insert_bst(root,data)
		i += 1

	return root

##################################

def printLevelWise(root):

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

#################################

def find_node(root,data):

	if(root == None):
		return None

	if(root.data == data):
		return root
	elif(root.data < data):
		return find_node(root.right,data)
	else:
		return find_node(root.left,data)

##################################

def inOrder(root):
	if(root != None):
		inOrder(root.left)
		print(root.data,end = " ")
		inOrder(root.right)

##################################

def find_max(root):
	if(root == None):
		return -1

	if(root.right == None):
		return root.data
	else:
		return find_max(root.right)

	#########################

def inorderPredecessor(root):

	if(root == None):
		return -1

	return find_max(root.left)

##################################

root = createBst()
inOrder(root)
print()
data = int(input("Enter data to find: "))
node = find_node(root,data)
print(inorderPredecessor(node)
