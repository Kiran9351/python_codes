import random

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

#################################

def createLL():
	
	n = random.randint(5,10)
	
	head = None
	prev = None
	i = 1;
	for i in range(n):
		i = i * 10;
		newNode = Node(random.randint(10*i,20*i))

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

def merge(head1,head2):

	head3 = None
	if(head1.data <= head2.data):
		head3 = head1
		head1 = head1.next
	else:
		head3 = head2
		head2 = head2.next
	temp = head3
	while(head1 != None and head2 != None):
		if(head1.data < head2.data):
			temp.next = head1
			head1 = head1.next
		else:
			temp.next = head2
			head2 = head2.next
		temp = temp.next

	if(head1 == None):
		temp.next = head2
	else:
		temp.next = head1

	return head3

##############################

head1 = createLL()
head2 = createLL()
printLL(head1)
printLL(head2)
newhead = merge(head1,head2)
printLL(newhead)
