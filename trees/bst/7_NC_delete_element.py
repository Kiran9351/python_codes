
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

################################

def insert_bst(root,data):
	if(root == None):
		root = Node(data)
	elif(root.data < data):
		root.right = insert_bst(root.right,data)
	elif(root.data > data):
		root.left = insert_bst(root.left,data)

	return root

	#######################

def creaetBst():

	n = int(input("Enter size of bst: "))
	
	root = None
	i = 1

	while(i < n):

		data = int(input("Enter data: "))
		root = insert_bst(root,data)
		i += 1

	return root

#################################

def find_min(root):
	if(root == None):
		return None

	if(root.left == None):
		return root
	else:
		return find_min(root.left)

	#########################

def find_node(root,data):
	if(root == None):
		return None

	if(root.data == data):
		return root
	elif(root.data < data):
		return find_node(root.right,data)
	else:
		return find_node(root.left,data)

	##########################

def delete_node(root,node):
	
	if(root == None):
		return 
	temp = root
	while(temp != node):
		parent = temp
		if(temp.data < node.data):
			temp = temp.right
		else:
			temp = temp.left

	# if only left child is there

	if(parent.left == node):
		if(node.right == None and node.left == None):
			parent.left = None
			del node
		elif(node.left == None):
			parent.left = node.right
		elif(node.right == None):
			parent.left = node.left
		else:
			min_node = find_min(node.right)
			

