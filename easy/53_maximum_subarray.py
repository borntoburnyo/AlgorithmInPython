class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            # Determines if it is worth to add previous element
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray(self, nums):
        def findOptimalSub(nums, left, right):
            if left > right:
                return -math.inf
            else:
                mid = (left + right) // 2
                cur = leftHalf = rightHalf = 0

                for i in range(mid-1, left-1, -1):
                    cur += nums[i]
                    leftHalf = max(leftHalf, cur)

                cur = 0
                for i in range(mid+1, right+1, 1):
                    cur += nums[i]
                    rightHalf = max(rightHalf, cur)

                crossMax = nums[mid] + leftHalf + rightHalf

                leftMax = findOptimalSub(nums, left, mid - 1)
                rightMax = findOptimaSub(nums, mid + 1, right)
                
                return max(crossMax, leftMax, rightMax)

        return findOptimalSub(nums, 0, len(nums) - 1)
