
def insertion_sort(arr):

	for i in range(1,len(arr)):
		temp = arr[i]
		k = i
		while(k > 0 and temp < arr[k-1]):
			arr[k] = arr[k-1]
			k -= 1

		arr[k] = temp

###################################

arr = [10,4,43,5,57,91,45,9,7]
insertion_sort(arr)
print(arr)
