
def bubble_sort(arr):
	
	for i in range(len(arr)-1,0,-1):
		for j in range(i):
			if(arr[j] > arr[j+1]):
				arr[j],arr[j+1] = arr[j+1],arr[j]

###################################

arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]
bubble_sort(arr)
print(arr)
