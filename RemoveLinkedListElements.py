'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


'''


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = None

        while(curr):
            if curr.val == val:
                if curr == head:
                    head = head.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return head
