# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-nodes-in-between-zeros
# source_path: LeetCode-Solutions-master/Python/merge-nodes-in-between-zeros.py
# solution_class: Solution
# submission_id: c35847d21be33dc464f9fe3d35e335e3ba9b4955
# seed: 2046470324

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


# linked list

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr, zero = head.next, head
        while curr:
            if curr.val:
                zero.val += curr.val
            else:
                zero.next = curr if curr.next else None
                zero = curr
            curr = curr.next
        return head