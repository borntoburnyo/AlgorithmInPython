class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]

        res = [[1]]
        row = 2
        while row <= numRow:
            # Add two 0's to both end of last row
            # The current row should be a rolling sum of two consecutive element in last row
            row_mod = [0] + res[-1] + [0]
            temp = []
            for i in range(len(row_mod)):
                if i + 1 < len(row_mod):
                    temp.append(row_mod[i] + row_mod[i+1])
            res.append(temp)
            row += 1

        return res

    def v2(self, numRows):
        # Populate return with the right length of 1's
        res = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            # Only need to update from the 2nd element
            for j in range(1, i):
                # The middle element is updated based on last row 
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
