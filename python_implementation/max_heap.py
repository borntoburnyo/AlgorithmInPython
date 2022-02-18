class MaxHeap:
	def __init__(self, nums=None):
		self.heap = []
		self.heap_size = 0
		if nums is not None:
			self.create_max_heap(nums)
			self.heap = nums
			self.heap_size = len(nums)

	def create_max_heap(self, nums):
		n = len(nums)	
		for i in range(n//2, -1, -1):
			self.max_heapify(nums, i, n)	

	def max_heapify(self, nums, i, n):
		lindex = i*2
		rindex = i*2 + 1
		largest = i
		if lindex < n:
			if nums[lindex] > nums[i]:
				largest = lindex
		if rindex < n:
			if nums[rindex] > nums[largest]:
				largest = rindex

		# if it gets swapped
		if largest != i:
			nums[i], nums[largest] = nums[largest], nums[i]
			self.max_heapify(nums, largest, n)
	
	def insert(self, item):
		self.heap.append(item)	
		self.heap_size += 1

		# make sure max heap property maintains
		idx = self.heap_size - 1	
		parent = idx // 2 	
		while parent >= 0 and self.heap[parent]	< self.heap[idx]:
			self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
			idx = parent
			parent = idx // 2
	def delete(self, index):
		# delete a node at index 
		# return the deleted value and maintain mas heap property
		if self.heap_size < 1:
			raise IndexError("Empty heap!")
	
		if index > self.heap_size - 1:
			raise IndexError("Index out-of-range!") 
		
		self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
		self.heap_size -= 1
		self.max_heapify(self.heap, index, self.heap_size)
	
		return self.heap.pop()

	def extract_max(self):
		return self.delete(0)	

	def increase_key(self, i, key):
		# increase the key of heap[i] to key
		if key < self.heap[i]:
			raise KeyError("The new key is smaller than the current key!")
		self.heap[i] = key
		# maintain the heap invariant
		parent = i // 2
		if i == 0:
			return
		while parent >= 0 and self.heap[parent] < self.heap[i]:
			self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
			i = parent
			parent = i // 2
		return 

	def print(self):
		return print(self.heap)

#hp1 = MaxHeap()
#print(hp1.delete(100))

hp = MaxHeap([0,3,2,10,8,5,6,9,21])
hp.print()

hp.insert(5)
hp.print()

hp.insert(100)
hp.print()

print(hp.delete(3))
print(hp.extract_max())

#hp.delete(100)
hp.increase_key(0, 10000)
hp.print()
hp.increase_key(3, 20000)
hp.print()
