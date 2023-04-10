import queue

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

##################################

def insert_bst(root,data):
	if(root == None):
		root = Node(data)
		return root

	if(root.data == data):
		return root
	elif(root.data < data):
		root.right = insert_bst(root.right,data)
	else:
		root.left =  insert_bst(root.left,data)
	
	return root
	##########################

def createBst():
	
	n = int(input("Enter size of bst : "))
	root = None
	i = 0
	while(i < n):
		data = int(input("Enter data: "))
		root = insert_bst(root,data)
		i += 1
	
	return root

##################################
	
def printlevelwise(root):

	if(root == None):
		return 
	
	q = queue.Queue()

	q.put(root)

	while(q.empty() != True):

		node = q.get()
		
		print(node.data,end = " : ")
		if(node.left != None):
			print("L "+ str(node.left.data),end = " ")
			q.put(node.left)

		if(node.right != None):	
			print("R "+str(node.right.data))
			q.put(node.right)

		print()
	
###############################	

root = createBst()
printlevelwise(root)
