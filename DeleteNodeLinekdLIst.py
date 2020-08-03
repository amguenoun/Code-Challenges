'''
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.
'''


def deleteNode(self, node):

    while node.next:
        node.val = node.next.val
        if node.next.next:
            node = node.next
        else:
            # tail
            node.next = None
