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

    def v2(self, triangle):
        # Use bottom-up way to update the minimum path sum
        below = triangle[-1]
        n = len(triangle)
        for row in range(n-2, -1, -1):
            cur = []
            # The smallest would be min(i, i+1) if you watch 
            # the triangle from bottom up
            # Since every element from next row will have two elements
            # from current row
            for col in range(row+1):
                smallest = min(below[col], below[col+1])
                cur.append(triangle[row][col] + smallest)
            below = cur

        return below[0]
