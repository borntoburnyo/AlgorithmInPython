class Solution:
    def v1(self, l1, l2):
        res = ListNode()
        head = res
        while l1 and l2:
            if l1.val >= l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next

        if l1:
            res.next = l1
        else:
            res.next = l2
        
        return head.next

    def v2(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.v2(l1.next, l2)
            return l1
        else:
            l2.next = self.v2(l1, l2.next)
            return l2
