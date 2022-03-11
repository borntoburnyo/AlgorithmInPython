class Solution:
    def rotateRight(self, head, k):
    # If empty list
    if not head:
        return None
    if not head.next:
        return head 

    # Get the list length and close the circle
    n = 1
    oldTail = head
    while oldTail.next:
        oldTail = oldTail.next
        n += 1
    oldTail.next = head

    # Find new tail and head 
    # New tail should be n - k % n - 1
    newTail = head 
    for i in range(n - k % n - 1):
        newTail = newTail.next
    newHead = newTail.next

    # Break the circle
    newTail.next = None

    return newHead

# Time complexity: O(N), N is the size of the list
# Space complexity: O(1) 
