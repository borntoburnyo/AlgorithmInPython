class Solution:
    def findDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        while high - low > 1:
            count = 0
            for k in nums:
                if mid < k < high:
                    count += 1
            if count > high - mid:
                low = mid 
            else:
                high = mid
            mid = (high + low) // 2

        return high

# Use bi-section method, similar to the binary search method

    def findDuplicate(self, nums):
        slow = nums[nums[0]]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow

# Use linked list concept
# The duplicate is the entrance of the circle
