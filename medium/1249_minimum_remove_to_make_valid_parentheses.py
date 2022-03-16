class Solution:
    def minRemoveToMakeValid(self, s):
        # Need a stack to store parentheses
        stk = []

        # Discretize the string for easy write
        ss = [x for x in s]

        # Loop through the splited string
        for i in range(len(ss)):
            # Push if left parenthese
            if not stk or ss[i] == '(':
                stk.append(i)
            # Pop if right parenthese
            elif stk and ss[i] == ')':
                stk.pop()
            # If no match left parentheses left for the coming right parenthese
            # overwrite the right parenthese with ''
            elif not stk and ss[i] == ')':
                ss[i] = ''

        # If the stack is not empty
        # there are extra left parentheses
        while stk:
            ss[stk.pop()] = ''

        return ''.join(ss)
