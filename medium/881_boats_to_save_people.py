class Solution:
    def numRescueBoats(self, people, limit):
        people.sort() # Start from heavist + lightest
        n = len(people)
        i, j = 0, n - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
                i += 1
            else:
                j -= 1

        return n - j - 1
