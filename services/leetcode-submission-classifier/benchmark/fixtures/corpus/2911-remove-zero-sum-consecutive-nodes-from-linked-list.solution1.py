# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-zero-sum-consecutive-nodes-from-linked-list
# source_path: LeetCode-Solutions-master/Python/remove-zero-sum-consecutive-nodes-from-linked-list.py
# solution_class: Solution
# submission_id: 834b85b425a9a8ccd2172eaec0fd62f7ba2664d5
# seed: 3560651499

# Time:  O(n)
# Space: O(n)

import collections


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        lookup = collections.OrderedDict()
        while curr:
            prefix += curr.val
            node = lookup.get(prefix, curr)
            while prefix in lookup:
                lookup.popitem()
            lookup[prefix] = node
            node.next = curr.next
            curr = curr.next
        return dummy.next