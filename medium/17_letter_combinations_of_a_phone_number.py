class Solution:
    def letterCombination(self, digits):
        letterMap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        if not digits:
            return res

        self.bfs(digits, 0, '', res, letterMap)
        return res

    def bfs(self, digits, index, tempRes, res, lMap):
        if index > len(digits) - 1:
            res.append(tempRes)
            return
        else:
            letters = lMap[digits[index]]
            for letter in letters:
                self.bfs(digits, index + 1, tempRes + letter, res, lMap)


# Return all possible combination is can be achieved by Breadth-First-Search tree structure
