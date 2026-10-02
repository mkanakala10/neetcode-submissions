# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        res = ListNode(-1)

        node = prev
        start = head
        while node.next:
            temp1 = start.next
            temp2 = node.next

            start.next = node
            node.next = temp1

            start = temp1
            node = temp2
            
        
