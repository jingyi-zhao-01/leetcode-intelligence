# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-the-middle-node-of-a-linked-list
# source_path: LeetCode-Solutions-master/Python/delete-the-middle-node-of-a-linked-list.py
# solution_class: Solution
# submission_id: 783ee7aaebbb1e215c8374add4fb7eda32727d38
# seed: 1639256837

# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        slow.next = slow.next.next
        return dummy.next