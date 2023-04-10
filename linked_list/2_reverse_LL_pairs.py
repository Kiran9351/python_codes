

class Node:
	
	def __init__(self,data):
		self.data = data
		self.next = None

###############################

def createLL():
	n = int(input("Enter number of elements in LL : "))
	
	head = None
	prev = None

	for i in range(n):
		data = int(input("Enter element at index " + str(i)+ " : "))

		newNode = Node(data)

		if(head != None):
			prev.next = newNode
			prev = newNode
		else:
			head = newNode
			prev = head

	return head

###############################

def printLL(head):
	while(head != None):
		print("|"+str(head.data)+"|->",end="")
		head = head.next

	print()

##############################

def pairs(first,second):
	temp = second.next
	second.next = first
	first.next = temp

	return second


def reverse_pairs(head):

	if(head == None or head.next == None):
		return head

	#temp = head
	#prev = head
	#head = head.next	

	#while(temp != None):
		
	#	temp = pairs(temp,temp.next)
		
	#	if(temp != head):
	#		prev.next = temp
	#		prev = temp.next

	#	temp = temp.next.next

	#return head		

	temp = head.next.next
	newHead = head.next
	head.next.next = head
	head.next = temp 
	prev = newHead.next

	while(temp != None):
		temp = pairs(temp,temp.next)
		prev.next = temp
		prev = temp.next
		temp = temp.next.next
	

	return newHead

###############################

head = createLL()
printLL(head)
head = reverse_pairs(head)
printLL(head)
print("Kiran")
