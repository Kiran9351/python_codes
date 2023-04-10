
import queue

class Node:

	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

##################################

def createBT():
	
	n = int(input("Enter size of BT : "))

	root = Node(int(input("Enter root data : ")))

	q = queue.Queue()

	q.put(root)

	i = 1

	while(q.empty() != True and i < n):
		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data)+" : "))
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

#################################

def preOrder(root):
	if(root != None):
		print(root.data,end = " ")
		preOrder(root.left)
		preOrder(root.right)

################################

def height_BT(root):
	
	if(root == None):
		return 0

	left = height_BT(root.left)
	right= height_BT(root.right)
	
	return max(left,right) + 1
	
	#########################

def diameter_BT(root):

	if(root == None):	
		return 0

	left = height_BT(root.left)
	right = height_BT(root.right)

	return left + right + 1

###################################

root = createBT()
preOrder(root)
print()
print(diameter_BT(root))
