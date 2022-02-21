def findMinMax(nums):
	if len(nums) // 2 == 0:
		R = [nums[0] if nums[0] < nums[1] else nums[1]]*2
	else:
	    R = [nums[0]]*2

	for i in range(1,len(nums)-1, 2):
		if nums[i] < nums[i+1]:
			R[0] = R[0] if R[0] < nums[i] else nums[i]
			R[1] = R[1] if R[1] > nums[i+1] else nums[i+1]
		else:
			R[0] = R[0] if R[0] < nums[i+1] else nums[i+1]
			R[1] = R[1] if R[1] > nums[i] else nums[i]

	return R

print(findMinMax([0,-3,4,10,-9,2]))
