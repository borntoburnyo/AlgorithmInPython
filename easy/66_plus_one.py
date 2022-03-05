class Solution:
    def plusOne(self, digits):
        dek = deque()
        inc = 1 # Use as both increment and the first 1 added
        for i in range(len(digits)-1, -1, -1):
            # If the last digit is 9
            # Or intermediate digit is 9 and have increment 1 to be added
            if inc == 1 and digits[i] == 9:
                dek.appendleft(0)
                inc = 1
            else:
                dek.appendleft(digits[i] + inc)
                inc = 0
        # Extend the digits if needed
        if inc == 1:
            dek.appendleft(1)

        return dek
