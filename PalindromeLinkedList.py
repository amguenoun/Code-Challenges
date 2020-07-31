'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true
'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        dummy = head
        while dummy:
            stack.append(dummy.val)
            dummy = dummy.next
        while head:
            if stack.pop() != head.val:
                return False
            else:
                head = head.next
        return True
