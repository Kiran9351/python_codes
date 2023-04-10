
import queue

class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

###################################

def createBT():
	n = int(input("Enter no. of nodes : "))
	
	root = Node(int(input("Enter root data: ")))
	
	q = queue.Queue()

	q.put(root)
	
	i = 1

	while(q.empty() != True and i < n):
		node = q.get()

		left_data = int(input("Enter left data of " + str(node.data) + " : "))
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

################################

def printBT(root):
	
	if(root == None):
		return

	q = queue.Queue()

	q.put(root)

	while(q.empty() != True):
		node = q.get()

		print(node.data,end = " : ")

		if(node.left != None):
			print("L "+str(node.left.data),end= " ")
			q.put(node.left)

		if(node.right != None):
			print("R "+str(node.right.data))
			q.put(node.right)

		print()

##############################

def create_mirror(root):
	
	if(root == None):
		return None
	
	mroot = Node(root.data)

	q = queue.Queue()
	qm = queue.Queue()

	q.put(root)
	qm.put(mroot)

	while(q.empty() != True):

		node = q.get()
		mnode = qm.get()

		if(node.left != None):
			mnode.right = Node(node.left.data)
			q.put(node.left)
			qm.put(mnode.right)

		if(node.right != None):
			mnode.left = Node(node.right.data)
			q.put(node.right)
			qm.put(mnode.left)

	return mroot

################################

def create_mirror_recur(root):
		
	if(root == None):
		return None

	mroot = Node(root.data)

	mroot.right = create_mirror_recur(root.left)
	mroot.left = create_mirror_recur(root.right)

	return mroot


###############################

def transform_mirror(root):

	if(root != None):
		transform_mirror(root.left)
		transform_mirror(root.right)
		
		temp = root.right
		root.right = root.left
		root.left = temp

	return root

##############################

root = createBT()
printBT(root)
mroot = create_mirror(root)
print()
printBT(mroot)
print()
print()
mroot1 = create_mirror(root)
printBT(mroot1)
transform_mirror(root)
printBT(root)
