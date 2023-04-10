
import random

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

#################################

def createCLL():
	
	n = random.randint(10,15)
	
	head = None
	prev = None

	for i in range(n):
		newNode = Node(random.randint(10,100))

		if(head != None):
			prev.next = newNode
			prev = newNode
		else:
			head = newNode
			prev = newNode

	prev.next = head
	
	return head,prev

##################################

def printCLL(head):
	
	if(head == None):
		return

	print("|"+str(head.data)+"|->",end = "")

	temp = head.next
	while(temp != head):
		print("|"+str(temp.data)+"|->",end="")
		temp = temp.next

	print()

#################################

def printLL(head):
	while(head != None):
		print("|"+str(head.data)+"|->",end = "")
		head = head.next
	
	print()

##################################

def chk_CLL(head):

	if(head == None):
		return False

	temp = head.next

	while(head != temp):
		temp= temp.next
		if(temp == None):
			return False
	
	return True

##################################

def split(head):

	if(head == None):
		return
	
	slow = head
	fast = head

	while(fast.next.next != head and fast.next != head):
		fast = fast.next.next
		slow = slow.next

	head1 = slow.next
	slow.next = None

	if(fast.next == head):
		fast.next = None
	else:
		fast.next.next = None

	return head,head1

###################################

head,prev = createCLL()
printCLL(head)
head,head1 = split(head)
printLL(head)
printLL(head1)
