# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-twin-sum-of-a-linked-list
# source_path: LeetCode-Solutions-master/Python/maximum-twin-sum-of-a-linked-list.py
# solution_class: Solution
# submission_id: 371542fa4385f94a49741492a3dca86cca5363c2
# seed: 2171588437

# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        def reverseList(head):
            dummy = ListNode()
            while head:
                dummy.next, head.next, head = head, dummy.next, head.next
            return dummy.next

        dummy = ListNode(next=head)
        slow = fast = dummy
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        result = 0
        head2 = reverseList(slow)
        while head:
            result = max(result, head.val+head2.val)
            head, head2 = head.next, head2.next
        return result