class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        res = []

        # Add intervals before the new one
        while not res or res[-1][0] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Add the new one and merge if needed 
        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newInterval[1])

        # Add remaining ones and merge if needed 
        while i < n:
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res

