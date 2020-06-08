'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        fp = head

        while fp.next is not None:
            if fp.val == fp.next.val:
                fp.next = fp.next.next
            else:
                fp = fp.next
        return head
