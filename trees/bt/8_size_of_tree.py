import queue

class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

################################

def createBT():
	
	n = int(input("Enter size of input : "))
	
	root = Node(int(input("Enter root data : ")))
	
	q = queue.Queue()

	q.put(root)
	i = 1
	while(q.empty() != True and i < n):
		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data)+" : "))
		if(left_data != -1 and i < n):
			node.left = Node(left_data)
			i += 1
			q.put(node.left)

		right_data = int(input("Enter right data of "+str(node.data)+ " : "))
		if(right_data != -1 and i < n):
			node.right = Node(right_data)
			i += 1
			q.put(node.right)
		
	return root

###################################

def printLevelWise(root):

	if(root == None):
		print("Tree is empty")
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

###################################

def size_BT(root):

	if(root == None):
		return 0

	left = size_BT(root.left)
	right = size_BT(root.right)

	return left + right + 1

#################################

root = createBT()
printLevelWise(root)
print(size_BT(root))
