# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-cycle
# source_path: LeetCode-Solutions-master/Python/linked-list-cycle.py
# solution_class: Solution
# submission_id: de376e0301c231021caca59283d1d26c0e538f45
# seed: 4005259983

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                return True
        return False