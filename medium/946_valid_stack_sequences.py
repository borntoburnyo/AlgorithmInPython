class Solution:
    def validateStackSequences(self, pushed, popped):
        # Need a pointer for popped 
        i = 0

        # Need a stack to loop through the process 
        stk = []

        for x in pushed:
            stk.append(x)
            while stk and stk[-1] == popped[i]:
                stk.pop()
                i += 1

        return True if not stk else False
