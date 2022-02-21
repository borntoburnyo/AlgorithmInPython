import random

def RandomizedSelect(nums, p, r, i):
	if p == r:
		return nums[p]
	
	# Randomized partition
	q = RandomizedPartition(nums, p, r)
	k = q - p + 1
	if k == i:
		return nums[q]
	elif i < k:
		return RandomizedSelect(nums, p, q-1, i)
	else:
		return RandomizedSelect(nums, q+1, r, i-k)

def Partition(nums, p, r):
	x = nums[r-1] 
	i = p - 1
	for j in range(p,r-1):
		if nums[j] <= x:
			i += 1
			nums[i], nums[j] = nums[j], nums[i]
	nums[r-1], nums[i+1] = nums[i+1], nums[r-1]
	return i+1

def RandomizedPartition(nums, p, r):
	i = random.randint(p, r)
	nums[r-1], nums[i] = nums[i], nums[r-1]
	return Partition(nums, p, r)

print(RandomizedSelect([-10,10,2,4,7,3], 0, 6, 5))
