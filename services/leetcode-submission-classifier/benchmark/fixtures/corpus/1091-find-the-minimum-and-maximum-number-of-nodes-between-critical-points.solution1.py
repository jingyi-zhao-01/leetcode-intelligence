# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-minimum-and-maximum-number-of-nodes-between-critical-points
# source_path: LeetCode-Solutions-master/Python/find-the-minimum-and-maximum-number-of-nodes-between-critical-points.py
# solution_class: Solution
# submission_id: 235d2978fe71830db63e239ae20d0c94f3c0c4d2
# seed: 759186013

# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        first = last = -1
        result = float("inf")
        i, prev, head = 0, head.val, head.next
        while head.next:
            if max(prev, head.next.val) < head.val or min(prev, head.next.val) > head.val:
                if first == -1:
                    first = i
                if last != -1:
                    result = min(result, i-last)
                last = i
            i += 1
            prev = head.val
            head = head.next
        return [result, last-first] if last != first else [-1, -1]