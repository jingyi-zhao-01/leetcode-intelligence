# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-list
# source_path: LeetCode-Solutions-master/Python/rotate-list.py
# solution_class: Solution
# submission_id: a06d7ffdab8e7be5a0b477286ea21f9b0966ceba
# seed: 3367121286

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        n, cur = 1, head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head

        cur, tail = head, cur
        for _ in xrange(n - k % n):
            tail = cur
            cur = cur.next
        tail.next = None

        return cur