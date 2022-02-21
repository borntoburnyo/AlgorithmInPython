def findMinMax(nums):
	if len(nums) // 2 == 0:
		R = [min(nums[0], nums[1])]*2
	else:
	    R = [nums[0]]*2

	for i in range(1,len(nums)-1, 2):
		small = min(nums[i], nums[i+1])
		R[0] = min(small, R[0])	
		large = max(nums[i], nums[i+1])
		R[1] = max(large, R[1])

	return R

print(findMinMax([0,-3,4,10,-9,2]))
