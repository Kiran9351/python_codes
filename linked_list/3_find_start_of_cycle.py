
import random

class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

###############################

def createLL():
	
	print("Taking size of LL and elements of LL randomly")

	n = random.randint(0,100)

	head = None
	prev = None

	for i in range(n):
		newHead = Node(random.randint(0,100))

		if(head != None):
			prev.next = newHead
			prev = newHead
		else:
			head = newHead
			prev = newHead

	return head,n

#################################

def printLL(head):
	while(head != None):
		print("|" + str(head.data) + "|->",end = "")
		head = head.next

	print()

#################################

def create_cycle(head,size):

	n = random.randint(0,size)

	temp = head
	last = head

	for i in range(n-1):
		temp = temp.next

	while(last.next != None):
		last = last.next
	
	print(temp.data)

	last.next = temp
	
	return head
#################################

def find_first(head):

	slow = head
	fast = head

	while(1):
		slow = slow.next
		fast = fast.next.next
		if(slow == fast):
			break
	
	slow = head
	
	while(slow != fast):
		slow = slow.next
		fast = fast.next
	
	return slow

################################

head,size = createLL()
printLL(head)
head = create_cycle(head,size)
node = find_first(head)
print(node.data)
