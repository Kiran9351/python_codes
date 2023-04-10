
def binary_search_recur(arr,low,high,data):
	
	if(low > high):
		return -1	

	mid = (low + high)//2
	if(arr[mid] == data):
		return mid
	elif(arr[mid] < data):
		return binary_search_recur(arr,mid+1,high,data)
	else:
		return binary_search_recur(arr,low,mid-1,data)

#######################################

def binary_search_iter(arr,data):

	low = 0
	high = len(arr)-1

	while(low <= high):
		mid = (low + high)//2
		if(arr[mid] == data):
			return mid
		elif(arr[mid] > data):
			high = mid-1
		else:
			low = mid + 1

	return -1

################################

arr = [534,246,933,127,277,321,454,565,220]
data = int(input("Enter data : "))
print(binary_search_iter(arr,data))
print(binary_search_recur(arr,0,len(arr)-1,data))
