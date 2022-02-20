def CountingSort(A, k):
	C = [0 for i in range(k)]
	for j in range(len(A)):
		C[A[j]] += 1
	for i in range(k):
		C[i] = C[i] + C[i-1]
	B = []
	for j in range(len(A)-1, -1, -1):
		B[C[A[j]]] = A[j]	
		C[A[j]] -= 1

	return B

print(CountingSort([2,5,3,0,2,3,0,3], 6))
