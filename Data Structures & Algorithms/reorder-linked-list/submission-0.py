# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node = slow.next
        prev = slow.next = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        first = head
        second = prev
        while first and second:
            prev = first.next
            prevsec = second.next

            first.next = second
            second.next = prev

            first = second.next
            second = prevsec
        
