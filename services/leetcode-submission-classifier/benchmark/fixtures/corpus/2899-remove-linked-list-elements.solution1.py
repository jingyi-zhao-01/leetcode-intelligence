# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-linked-list-elements
# source_path: LeetCode-Solutions-master/Python/remove-linked-list-elements.py
# solution_class: Solution
# submission_id: ebc9044f8e6cad8865764836be4496c3866c6409
# seed: 2922913041

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev, curr = dummy, dummy.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next