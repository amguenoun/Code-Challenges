'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def returnLinkedNumber(self, l1: ListNode):
        num = ''
        while l1 is not None:
            num = str(l1.val) + num
            l1 = l1.next
        return int(num)

    def createLinkedNumber(self, number):
        lastPlace = str(number)[-1]
        remainder = str(number)[:-1]

        linkedListHead = ListNode(int(lastPlace))
        pointer = linkedListHead

        while len(remainder) > 0:
            lastPlace = str(remainder)[-1]
            remainder = str(remainder)[:-1]

            nextNode = ListNode(int(lastPlace))
            pointer.next = nextNode
            pointer = nextNode

        return linkedListHead

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        firstNumber = self.returnLinkedNumber(l1)
        secondNumber = self.returnLinkedNumber(l2)

        total = firstNumber + secondNumber

        head = self.createLinkedNumber(total)

        return head
