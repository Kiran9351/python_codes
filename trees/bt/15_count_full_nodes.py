import queue

class Node:
	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

#################################

def createBT():

	n = int(input("Enter size of tree : "))
	
	root = Node(int(input("Enter root data : ")))
	
	q = queue.Queue()
	q.put(root)
	i = 1

	while(q.empty() != True and i < n):

		node = q.get()

		left_data = int(input("Enter left data of "+str(node.data)+" : "))

		if(left_data != -1):
			node.left = Node(left_data)
			q.put(node.left)
			i += 1
		
		if(i >= n):
			break		

		right_data = int(input("Enter right data of "+str(node.data) + " : "))
		if(right_data != -1):
			node.right = Node(right_data)
			q.put(node.right)
			i += 1

	return root

##############################

def height_BT(root):

	if(root == None):
		return 0

	left = height_BT(root.left)
	right = height_BT(root.right)

	return max(left,right) + 1

################################

def preOrder(root):

	if(root != None):
		print(root.data,end = " ")
		preOrder(root.left)
		preOrder(root.right)

###############################

def cnt_leaves(root):

	if(root == None):
		return 0

	q = queue.Queue()
	cnt = 0
	q.put(root)
	while(q.empty() != True):
		node = q.get()

		if(node.left == None and node.right == None):
			cnt += 1
		else:
			if(node.left != None):
				q.put(node.left)

			if(node.right != None):
				q.put(node.right)

	return cnt

###############################

def cnt_full(root):
	if(root == None):
		return 0

	q = queue.Queue()
	cnt = 0
	q.put(root)

	while(q.empty() != True):
		node = q.get()
		
		if(node.left != None and node.right != None):
			cnt += 1
		
		if(node.left != None):
			q.put(node.left)

		if(node.right != None):	
			q.put(node.right)

	return cnt

###############################

root = createBT()
preOrder(root)
print()
print(height_BT(root))

print(cnt_leaves(root))
print(cnt_full(root)
