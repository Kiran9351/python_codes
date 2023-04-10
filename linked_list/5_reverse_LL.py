
import random

class Node:

	def __init__(self,data):

		self.data = data
		self.next = None

################################

def createLL():

	print("Taking size of LL and elements of LL randomly:")

	n = random.randint(0,10)

	head = None
	prev = None

	for i in range(n):
		
		newNode = Node(random.randint(0,100))

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
		print("|"+str(head.data)+"|->",end="")
		head = head.next

	print()

################################

def reverse_LL(head):

	if(head == None or head.next == None):
		return head

	curr = head
	front = None
	prev = None

	while(curr != None):
		
		front = curr.next
		curr.next = prev
		prev = curr
		curr = front

	return prev

###############################

head = createLL()
printLL(head)
head = reverse_LL(head)
printLL(head)
