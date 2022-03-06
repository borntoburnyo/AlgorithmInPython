class Solution:
    def merge(self, nums1, m, nums2, n):
        # Do not use extra space
        # Modify nums1 in-place
        # Always see if start from backward of the array would help
        i = m - 1
        j = n - 1
        k = m + n - 1
        # While both nums are not "empty"
        while i >= 0 and j >= 0:
           if nums1[i] <= nums2[j]:
               nums1[k] = nums2[j]
               j -= 1
            else:
               nums1[k] = nums1[i]
               i -= 1
            k -= 1
        # If nums2 is not "empty"
        if j >= 0:
            nums1[:j] = nums2[:j]

        return nums1

