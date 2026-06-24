# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: swap-nodes-in-pairs
# source_path: LeetCode-Solutions-master/Python/swap-nodes-in-pairs.py
# solution_class: Solution
# submission_id: 9b9eee0b2300946748efb3c18dd2ed7d472c430e
# seed: 3173875908

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.next