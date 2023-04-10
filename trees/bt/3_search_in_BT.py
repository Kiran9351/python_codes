
import queue

class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None

#################################

def createBT():

	n = int(input("Enter number of nodes in BT : "))

	rootdata = int(input("Enter root data : "))

	root = Node(rootdata)
	i = 1

	q = queue.Queue()

	q.put(root)

	while((q.empty() != True) and i < n):
		node = q.get()
		left_data = int(input("Enter left data of "+str(node.data)+" : "))
		if(left_data != -1):
			node.left = Node(left_data)
			q.put(node.left)
			i += 1
		
		right_data = int(input("Enter right data of :"+str(node.data)+" : "))
		if(right_data != -1):
			node.right = Node(right_data)
			q.put(node.right)
			i += 1

	return root

###################################

def printLevelWise(root):

	q = queue.Queue()

	q.put(root)

	while(q.empty() != True):

		node = q.get()

		print(node.data,end = ":")
		if(node.left != None):
			print("L "+str(node.left.data),end = " ")
			q.put(node.left)

		if(node.right != None):
			print("R "+str(node.right.data),end="")
			q.put(node.right)

		print()

#####################################

def search(root,val):

	if(root == None):
		return False

	if(root.data == val):
		return True

	left_search = search(root.left,val)
	right_search = search(root.right,val)

	return (left_search or right_search)

#####################################
root = createBT()
printLevelWise(root)

bRet = search(root,int(input("Enter data to search: ")))
print(bRet)	
