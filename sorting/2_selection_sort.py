# selection sort

def selection_sort(arr):
	for i in range(len(arr) - 1):
		minindex = i
		for j in range(i,len(arr)):
			if(arr[j] < arr[minindex]):
				arr[j],arr[minindex] = arr[minindex],arr[j]


######################################

arr = [10,4,43,5,57,91,45,9,7]
selection_sort(arr)
print(arr)
