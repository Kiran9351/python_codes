
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

def even_odd(head):
	if(head == None):
		return 1
	
	fast = head
	while(fast != None and fast.next != None):
		fast = fast.next.next

	if(fast == None):
		return 1
	else:
		return 0

##############################

head = createLL()
printLL(head)
print("Even") if (even_odd(head) == 1) else print("Odd")
