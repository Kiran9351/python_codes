
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

#################################

def createLL():
	
	n = int(input("Enter size of linked list : "))
	
	head = None
	prev = None

	for i in range(n):
		newNode = Node(int(input("Enter data : ")))

		if(head != None):
			prev.next = newNode
			prev = newNode
		else:
			head = newNode
			prev = newNode

	return head

###############################

def printLL(head):
	while(head != None):
		print("|"+str(head.data)+"|->",end = "")
		head = head.next

	print()

##############################

def display_rev(head):
	
	if(head == None):
		return

	s = []

	while(head != None):
		s.append(head.data)
		head = head.next

	while(len(s) != 0):
		print("<-|"+str(s.pop())+"|",end="")
	
	print()

#################################

head = createLL()
printLL(head)
display_rev(head)
