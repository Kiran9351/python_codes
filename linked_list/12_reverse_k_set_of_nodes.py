import random

class Node:
	def __init__(self,data):

		self.data = data
		self.next = None

################################

def createLL():

	n = random.randint(10,15)

	head = None
	prev = None
	
	for i in range(n):
		newNode = Node(random.randint(10,50))

		if(head != None):
			prev.next = newNode
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

#################################

def reverse_k_nodes(head,k):
	
	if(head == None or k <= 0):
		return head

	front = head.next
	first = head
	back = head
	i = 0	
	while(front != None and i < k - 1):
		temp = front.next
		front.next = back
		back = front
		front = temp
		i += 1

	first.next = front
	first.next = reverse_k_nodes(first.next,k)

	return back

#################################

head = createLL()
printLL(head)
head = reverse_k_nodes(head,int(input("Enter k: ")))
printLL(head)	
