def insertionSort(arr): 
	for i in range(1, len(arr)): 
		key = arr[i] 
		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key
l=[4,85,48,24,8,14,154,155]
insertionSort(l)
print(l)
