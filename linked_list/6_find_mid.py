
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

def find_mid(head):
	if(head == None):
		return -1,None

	fast = head
	slow = head

	while(fast.next != None and fast.next.next != None):
		fast = fast.next.next
		slow = slow.next

	return slow.data,slow

#################################

head = createLL()
printLL(head)
val,node = find_mid(head)
print(val)
print(node.data)
