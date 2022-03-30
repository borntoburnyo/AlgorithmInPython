class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        while left <= right:
        if target <= matrix[left][right]:
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[left][mid] == target:
                    return True
                elif matrix[left][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            break
        else:
            left += 1
        
        return False

    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1 
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
