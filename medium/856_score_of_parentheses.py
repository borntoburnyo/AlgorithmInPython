class Solution:
    def scoreOfParentheses(self, s):
        stk = [] # Store temp score for each char
        score = 0
        for x in s:
            if x == '(': # Append score from last round update
                stk.append(score)
                score = 0
            else:
                score = stk[-1] + max(2*score, 1)
                stk.pop()

        return score
