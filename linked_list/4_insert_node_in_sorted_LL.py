
class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

################################

def createLL():

	n = int(input("Enter size of LL: "))

	head = None
	prev = None

	for i in range(n):

		newNode = Node(int(input("Enter element no. " + str(i) + " : ")))

		if(head != None):
			prev.next = newNode
			prev = newNode
		else:
			head = newNode
			prev = newNode

	return head

################################

def printLL(head):

	while(head != None):
		print("|"+str(head.data)+"|->",end = "")
		head = head.next

	print()

###############################

def insert_node(head,data):
	
	if(head != None):

		temp = head
		prev = temp
	
		while(temp.data < data):
			prev = temp
			temp = temp.next

		newNode = Node(data)

		newNode.next = prev.next
		prev.next = newNode
	else:
		head = Node(data)

	return head

################################

head = createLL()
printLL(head)
data = int(input("Enter data to insert : "))
head = insert_node(head,data)
printLL(head)
