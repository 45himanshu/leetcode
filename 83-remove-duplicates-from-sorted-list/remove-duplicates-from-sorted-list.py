# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        # edge case
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
        return head


        