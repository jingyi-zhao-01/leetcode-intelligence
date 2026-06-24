# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-cycle-ii
# source_path: LeetCode-Solutions-master/Python/linked-list-cycle-ii.py
# solution_class: Solution
# submission_id: c8ee2a211c69ec5ba46fa35a33485c9b9d31647c
# seed: 936347596

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self:
            return "{}".format(self.val)
        else:
            return None

class Solution(object):
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None