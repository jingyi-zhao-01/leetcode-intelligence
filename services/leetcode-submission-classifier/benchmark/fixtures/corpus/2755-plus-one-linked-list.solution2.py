# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: plus-one-linked-list
# source_path: LeetCode-Solutions-master/Python/plus-one-linked-list.py
# solution_class: Solution2
# submission_id: 302235c69ad7cf8c050d7133d11304278ec43022
# seed: 1917394235

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Two pointers solution.

class Solution2(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverseList(head):
            dummy = ListNode(0)
            curr = head
            while curr:
                dummy.next, curr.next, curr = curr, dummy.next, curr.next
            return dummy.next

        rev_head = reverseList(head)
        curr, carry = rev_head, 1
        while curr and carry:
            curr.val += carry
            carry = curr.val / 10
            curr.val %= 10
            if carry and curr.next is None:
                curr.next = ListNode(0)
            curr = curr.next

        return reverseList(rev_head)