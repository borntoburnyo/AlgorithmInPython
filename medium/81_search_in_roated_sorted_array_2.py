class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            while left < mid and nums[left] == nums[mid]:
                left += 1
            
            # If left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If right half is sorted
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

# Utilize the property that the list is sorted in the two half
# Only conduct binary search in the sorted half
# Tricky part is to make sure the judgement on the left half is correct
# e.g., [1,0,1,1,1], we need to shift the left index until the left value is
# not equal to the mid. And this can be achieved by shifting the right index as well
