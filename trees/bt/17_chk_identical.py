
import queue

class Node:
	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

##################################

def createBT():
	
	n = int(input("Enter number of nodes in binary tree: "))
	
	root = Node(int(input("Enter root data : ")))

	q = queue.Queue()
	q.put(root)

	i = 1

	while(q.empty() != True and i < n):

		node = q.get()
	
		left_data = int(input("Enter left data of "+str(node.data) + " : "))
		if(left_data != -1):
			node.left = Node(left_data)
			q.put(node.left)
			i += 1

		right_data = int(input("Enter right data of "+str(node.data)+ " : "))

		if(right_data != -1):
			node.right = Node(right_data)
			q.put(node.right)
			i += 1

	return root

#################################

def preOrder(root):

	if(root != None):
		print(root.data,end = " ")
		preOrder(root.left)
		preOrder(root.right)

################################

def chk_identical(rootl,rootr):

	if(rootl == None and rootr == None):
		return True
	
	if((rootl == None and rootr != None) or (rootl != None and rootr == None)):
		return False	

	if(rootl.data != rootr.data):
		return False

	left = chk_identical(rootl.left,rootr.left)
	right = chk_identical(rootl.right,rootr.right)

	return (left and right)

#################################

rootl = createBT()
preOrder(rootl)
print()
rootr = createBT()
preOrder(rootr)
print()

print(chk_identical(rootl,rootr))
