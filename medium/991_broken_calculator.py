class Solution:
    def brokenCalc(self, startValue, target):
        count = 0
        while startValue != target: # Working backward, multiply 2 becomes divided by 2, minus 1 becomes plus 1
            if startValue > target: # Trivial case
                return startValue - target
            else:
                if target % 2 == 0: # Even number is trivial
                    target //= 2
                else: # Make odd number become even
                    target += 1

            count += 1

        return count
