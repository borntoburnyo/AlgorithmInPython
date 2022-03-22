from collections import deque

class Solution:
    def getSmallestString(self, n, k):
        i = 0
        # Need a deque container, since we need to construct the string from end backward
        dek = deque()

        while i < n:
            if k - 26 > n - i - 1: # If K is larger than 26, the remaining can at least fill in the rest place in the string with 'a'
                dek.appendleft(26)
                k -= 26
            else: # If not, put the largest possible character at the end 
                dek.appendleft(k - (n - i - 1))
                k = n - i - 1

            # Remember to increse the loop index
            i += 1

        # Convert the values in the deque to characters and form a string
        return "".join([chr(96+x) for x in dek])
