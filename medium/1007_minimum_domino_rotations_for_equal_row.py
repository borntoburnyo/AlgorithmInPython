class Solution:
    def minDominoRotations(self, tops, bottoms):
        # It suffice to just check the first element
        for x in [tops[0], bottoms[0]]:
            if all(x in z for z in zip(tops, bottoms)):
                return len(tops) - max(top.count(x), bottoms.count(x))
            else: # Continue to check bottoms[0]
                continue

        # If the 1st element is not in either top[i] or bottoms[i] for every i
        # it means there is not such equal row
        return -1
