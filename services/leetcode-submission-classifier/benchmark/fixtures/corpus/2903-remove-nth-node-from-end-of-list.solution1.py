# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-nth-node-from-end-of-list
# source_path: LeetCode-Solutions-master/Python/remove-nth-node-from-end-of-list.py
# solution_class: Solution
# submission_id: 65a78a0a83240cf262136527fee699c1787bb9c6
# seed: 2309107526

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in xrange(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next