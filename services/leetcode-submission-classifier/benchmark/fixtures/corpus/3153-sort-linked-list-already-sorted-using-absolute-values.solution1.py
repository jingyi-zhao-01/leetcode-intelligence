# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-linked-list-already-sorted-using-absolute-values
# source_path: LeetCode-Solutions-master/Python/sort-linked-list-already-sorted-using-absolute-values.py
# solution_class: Solution
# submission_id: a1e2753fa76d412bb0abbffa9c304a87bdd8b483
# seed: 561347698

# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortLinkedList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tail, curr, head.next = head, head.next, None
        while curr:
            if curr.val > 0:
                curr.next, tail.next, tail, curr = None, curr, curr, curr.next
            else:
                curr.next, head, curr = head, curr, curr.next
        return head