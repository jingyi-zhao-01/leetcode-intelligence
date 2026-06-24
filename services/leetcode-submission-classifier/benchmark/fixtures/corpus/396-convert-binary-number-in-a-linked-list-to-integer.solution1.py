# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-binary-number-in-a-linked-list-to-integer
# source_path: LeetCode-Solutions-master/Python/convert-binary-number-in-a-linked-list-to-integer.py
# solution_class: Solution
# submission_id: c39a70bf0f5da1dad73d22d7cc8f4bdee02347dd
# seed: 484787366

# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        result = 0
        while head: 
            result = result*2 + head.val 
            head = head.next 
        return result