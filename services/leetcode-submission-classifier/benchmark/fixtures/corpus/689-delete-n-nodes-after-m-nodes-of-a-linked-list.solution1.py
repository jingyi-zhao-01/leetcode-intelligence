# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-n-nodes-after-m-nodes-of-a-linked-list
# source_path: LeetCode-Solutions-master/Python/delete-n-nodes-after-m-nodes-of-a-linked-list.py
# solution_class: Solution
# submission_id: bb3522a403565571ce9351edc273c6e1350ee1bb
# seed: 2430226362

# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        head = dummy = ListNode(next=head)
        while head:
            for _ in xrange(m):
                if not head.next:
                    return dummy.next
                head = head.next
            prev = head
            for _ in xrange(n):
                if not head.next:
                    prev.next = None
                    return dummy.next
                head = head.next
            prev.next = head.next
        return dummy.next