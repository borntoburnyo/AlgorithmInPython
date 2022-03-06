def InsertionSort(nums):
	for j in range(1,len(nums)):
		key = nums[j]
		i = j - 1
        # Make sure elements with index < j stay increasing order
        # O/W, switch to push the biggest to the position of j-1
        # Just imagine how you shuffle a hand of pokers
		while i > -1 and nums[i] > key:
			nums[i+1], nums[i] = nums[i], nums[i+1]
			i -= 1
		nums[i+1] = key
	
	return nums

print(InsertionSort([5,2,4,6,1,3]))
