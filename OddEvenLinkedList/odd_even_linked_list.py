# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        odd, even = head, head.next

        # No point of checking odd. even list will always be shorter.
        while even and even.next:
            pointer = even.next
            even.next = even.next.next
            pointer.next = odd.next
            odd.next = pointer

            # Next iteration
            odd = odd.next
            even = even.next
        return head
