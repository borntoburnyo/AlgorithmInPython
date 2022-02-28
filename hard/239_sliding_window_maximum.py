from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        dek = deque()
        for i in range(len(nums)):
            # Maintain a dek with dek head is the maximum
            while dek and nums[dek[-1]] <= nums[i]:
                dek.pop()
            dek.append(i)

            # Pop dek head if it is not in the sliding window
            while dek and i - dek[0] >= k:
                dek.popleft()

            # Start output when pointer >= first window upper bound
            if i >= k - 1:
                res.append(nums[dek[0]])
            
        return res
