class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initiate the head of the results linked list
        resHead = res = ListNode()

        # Initiate the carry value
        carry = 0

        # Loop through both list
        while l1 or l2:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            # Populate node in the results list
            val = (val1 + val2 + carry) % 10
            res.next = ListNode(val)
            res = res.next
            carry = val // 10

        # If there is still 1 carry left
        if carry:
            res.next = ListNode(carry)


        return resHead.next
