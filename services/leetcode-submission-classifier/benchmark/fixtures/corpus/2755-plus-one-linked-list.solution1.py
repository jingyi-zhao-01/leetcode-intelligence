# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: plus-one-linked-list
# source_path: LeetCode-Solutions-master/Python/plus-one-linked-list.py
# solution_class: Solution
# submission_id: 521e2bdc778c66f68f709d2ea6782e821f9635bb
# seed: 2930866160

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Two pointers solution.

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, head
        while right.next:
            if right.val != 9:
                left = right
            right = right.next

        if right.val != 9:
            right.val += 1
        else:
            left.val += 1
            right = left.next
            while right:
                right.val = 0
                right = right.next

        return dummy if dummy.val else dummy.next