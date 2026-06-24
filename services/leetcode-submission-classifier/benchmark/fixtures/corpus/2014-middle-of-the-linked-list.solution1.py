# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: middle-of-the-linked-list
# source_path: LeetCode-Solutions-master/Python/middle-of-the-linked-list.py
# solution_class: Solution
# submission_id: 1fa6dd394b5817e41474897c434703f65478727c
# seed: 1037539496

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow