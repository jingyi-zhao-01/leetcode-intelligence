# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-linked-list
# source_path: LeetCode-Solutions-master/Python/reverse-linked-list.py
# solution_class: Solution2
# submission_id: 4b95f59b4d5de1cb9b7c5cb0f60800273a07f738
# seed: 2600190414

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# Iterative solution.

class Solution2(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin

    def reverseListRecu(self, head):
        if not head:
            return [None, None]

        [begin, end] = self.reverseListRecu(head.next)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]