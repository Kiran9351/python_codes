

class Node:
	
	def __init__(self,data):
		
		self.data = data
		self.next = None

################################

def createLL():
	
	print("Enter number of elemets in ll:")
	val = int(input())

	head = None
	prev = None

	for i in range(val):
		
		data = int(input("Enter data: "))
		newNode = Node(data)

		if(head == None):
			head = newNode
			prev = newNode
		else:
			prev.next = newNode
			prev = newNode

	return head

##################################

def merge_sort_list(head1,head2):
	
	newHead = None

	if(head1.data < head2.data):
		temp = head1
		head1 = head1.next
		newHead = temp
	elif(head2.data < head1.data):
		temp = head2
		head2 = head2.next
		newHead = temp
	else:
		temp = head1
		head1= head1.next
		temp.next = head2
		head2 = head2.next
		newHead = temp.next
		
	

	while(head1 != None and head2 != None):
		if(head1.data < head2.data):
			newHead.next = head1
			head1 = head1.next
		elif(head1.data > head2.data):
			newHead.next = head2
			head2 = head2.next
		else:
			newHead.next = head1
			head1 = head1.next
			newHead.next.next = head2
			head2 = head2.next
			newHead = newHead.next
		
		newHead = newHead.next
	
	if(head1 != None):
		newHead.next = head1

	if(head2 != None):
		newHead.next = head2	

	return temp

##################################

def printLL(head):
	while(head != None):
		print("|" +str(head.data)+"|->",end = "")
		head = head.next
	
	print()

#################################

head1 = createLL()
head2 = createLL()
printLL(head1)
printLL(head2)

mergeHead = merge_sort_list(head1,head2)
printLL(mergeHead)
