class Solution:
    def twoCitySchedCost(self, costs):
        # Add B-A as the 3rd value
        costs = [[x[0], x[1], x[1] - x[0]] for x in costs]

        # Sort reverse based on the 3rd value
        # x[1]-x[0] means the savings of flying to A
        # Then the first half of the sorted list will fly to A
        res = 0
        for i in range(len(costs) // 2):
            if i < len(costs) // 2:
                res += costs[i][0]
            else:
                res += costs[i][1]

        return res
