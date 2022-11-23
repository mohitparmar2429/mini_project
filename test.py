def linear_search(array,element):
    for i in range(len(array)):
        if (element == array[i]):
            return i+1
            break
    

def binary_search(array , low , high , element):
    if high >= low:
        mid = (high + low) // 2
        
        if array[mid] == element:
            print(mid)
        
        elif array[mid] > element:
            return binary_search(array,low,mid-1,element)
        
        else:
            return binary_search(array,mid+1,high,element)
    
    else:
        return -1


def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

        


def bubbleSort(arr):
	n = len(arr)
	# optimize code, so if the array is already sorted, it doesn't need
	# to go through the entire process
	swapped = False
	# Traverse through all array elements
	for i in range(n-1):
		# range(n) also work but outer loop will
		# repeat one time more than needed.
		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		print(arr)
		if not swapped:
			# if we haven't needed to make a single swap, we
			# can just exit the main loop.
			return


# Python program for implementation of Insertion Sort

# Function to do insertion sort
# def insertionSort(arr):
    

# 	# Traverse through 1 to len(arr)
# 	for i in range(1, len(arr)):
#         key = arr[i]

# 		# Move elements of arr[0..i-1], that are
# 		# greater than key, to one position ahead
# 		# of their current position
# 		j = i-1
# 		while j >=0 and key < arr[j] :
# 				arr[j+1] = arr[j]
# 				j -= 1
# 		arr[j+1] = key
#     print(arr)

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] =  arr[j]
            j-=1
        arr[j+1] = key
    print(arr)
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


# def mergeSort(arr, l, r):
# if l < r:
# # Same as (l+r)//2, but avoids overflow for
# # large l and h
# m = l+(r-l)//2

# # Sort first and second halves
# mergeSort(arr, l, m)
# mergeSort(arr, m+1, r)
# merge(arr, l, m, r)

def mergeSort(arr,l,r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)
    print(arr)
    

# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


def reversing_the_array(array):
    return array.reverse() # there's a function called reverse to do so

def remove_duplicate(array):
    arr = set(array) # set in python automatically removes duplicates
    return list(arr)


# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr


print("Select operation.")
print("1.linear search")
print("2.binary search")
print("3.selection sort")
print("4.bubble sort")
print("5.insertion sort")
print("6.mergesort")
print("7.quicksort")
print("8.reversing the array")
print("9.remove the duplicates")
print("10.rotate the array")
usr_input = input("\nchoose what do you need to do : \n")
array1 = list(map(int,input("the array please with space seperated values: ").split()))
if usr_input == "1":
    print("linear search is being done: ")
    element = int(input("please give the element you want to search: "))
    print(linear_search(array1,element))

elif usr_input == "2":
    print("binary search is being done: ")
    element = int(input("please give the element you want to search: "))
    print(binary_search(array1,0,len(array1)-1,element))


    
    
    
elif usr_input == "3":
    print("selection sort is being done: ")
#    element = int(input("please give the element you want to search: "))
    selectionSort(array1,len(array1))
    print(array1)
elif usr_input == "4":
    print("bubble sort is being done: ")
    #element = int(input("please give the element you want to search: "))
    print(bubbleSort(array1))
elif usr_input == "5":
    print("insertion sort is being done: ")
    #element = int(input("please give the element you want to search: "))
    insertionSort(array1)
    #print(array1)
elif usr_input == "6":
    print("mergesort is being done: ")
    #element = int(input("please give the element you want to search: "))
    print(mergeSort(array1,0,len(array1)-1))
    
elif usr_input == "7":
    print("quicksort is being done: ")
    #element = int(input("please give the element you want to search: "))
    quickSort(array1,0,len(array1)-1)
    print(array1)
elif usr_input == "8":
    print("reversing the array: ")
    #element = int(input("please give the element you want to search: "))
    reversing_the_array(array1)
    print(array1)
elif usr_input == "9":
    print("removing the duplicate.... ")
    #element = int(input("please give the element you want to search: "))
    print(remove_duplicate(array1))

elif usr_input == "10":
    print("rotating the array... ")
    element = int(input("please give the number of elements you want to rotate: "))
    print(rotateArray(array1,len(array1),element))
    
print("good day")
    

    
    


    
        
    
