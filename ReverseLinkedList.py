'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''


def reverseList(self, head: ListNode) -> ListNode:
    start = ListNode(0)
    while head:
        temp, newhead = start.next, head.next
        start.next, head.next = head, temp
        head = newhead
    return start.next
