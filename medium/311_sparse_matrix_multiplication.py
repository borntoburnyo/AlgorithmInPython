class Solution:
    def multiply(self, mat1, mat2):
        res = [[0] * len(mat2[0])] * len(mat1)

        for rowIndex, row_elements in enumerate(mat1):
            for element_index, row_element in enumerate(row_elements):
                if row_element:
                    for colIndex, col_element in enumerate(mat2[element_index]):
                        res[rowIndex][colIndex] += row_element * col_element
        return res
