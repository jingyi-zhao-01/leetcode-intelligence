# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-linked-list
# source_path: LeetCode-Solutions-master/Python/reverse-linked-list.py
# solution_class: Solution
# submission_id: 31be15f81b5dc6dddaed535f010d3873f7d9cf73
# seed: 2919442316

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

class Solution(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next