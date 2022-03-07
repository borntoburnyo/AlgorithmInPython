class Solution:
    def minimumTotal(self, triangle):
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                # Find smallest in last row that are connected to current cell
                smallest_last = math.inf
                if col > 0:
                    smallest_last = triangle[row-1][col-1]
                if col < row:
                    smallest_last = min(smallest_last, triangle[row-1][col])
                # Update each cell to contain the minimum path sum
                triangle[row][col] += smallest_last

        # The minimum of last row will be the final minimum path sum 
        return min(triangle[-1])
