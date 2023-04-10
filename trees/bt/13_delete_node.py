## Not done

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

def deepest_node(root):
	
	if(root == None):
		return None

	q = queue.Queue()
	q.put(root)

	while(q.empty() != True):
		node = q.get()

		if(node.left != None):
			q.put(node.left)

		if(node.right != None):
			q.put(node.right)

	return node

	###############################

def find_node(root,data):
	if(root == None):
		return None

	if(root.data == data):
		return root

	left = find_node(root.left,data)
	right = find_node(root.right,data)
	
	if(left != None):
		return left
	
	if(right != None):
		return right

	return None
	
	############################

def delete_node(root,data):
		
	if(root == None):
		return None

	if(root.data == data):
		return root 
	
	root.left = delete_node(root.left,data)
	root.right = delete_node(root.right,data)
	
	if(root.left != None and root.left.data == data):
		root.left = None
	if(root .right != None and root.right.data == data):
		root.right == None
	
	return root
	
	#############################

def arrangement_delete_node(root,data):

	if(root == None):
		return None

	node = find_node(root,data)
	deep_node = deepest_node(root)

	node.data = deep_node.data
	deep_node.data = data

	root = delete_node(root,data)

	return root
##############################

root = createBT()
preOrder(root)
print()
print(height_BT(root))
#print(deepest_node(root).data)
data = int(input("Enter data to be delete : "))
#print(find_node(root,data).data)
root = arrangement_delete_node(root,data)
preOrder(root)
