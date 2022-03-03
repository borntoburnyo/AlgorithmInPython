class Solution:
    def hasCycle(self, head):
        htable = set()
        while head:
            # If head appears before, then it's cyclic
            if head in htable:
                return True
            # Store head in the hash table
            htable.add(head)
            head = head.next
        return False

    # Just like one fast, one slow runner running in the same track
    # The fast runner will eventually meet the slow runner
    def space_o1_solution(self, head):
        if not head:
            return False
        slow = head 
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fase.next.next

        return True
