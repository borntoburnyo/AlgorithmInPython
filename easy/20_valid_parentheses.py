class Solution:
    def isValid(self, s):
        if not s:
            return True

        checkStack = []
        for i in range(len(s)):
            if not checkStack or s[i] in ['(', '[', '{']:
                checkStack.append(s[i])
            else:
                if self.isMatch(checkStack[-1], s[i]):
                    checkStack.pop()
                else:
                    return False

        return True if not checkStack else False

    def isMatch(self, ss1, ss2):
        if ss1 + ss2 in ['()', '[]', '{}']:
            return True
        else:
            return False
