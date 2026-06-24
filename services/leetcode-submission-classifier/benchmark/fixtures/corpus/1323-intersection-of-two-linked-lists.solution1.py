# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-two-linked-lists
# source_path: LeetCode-Solutions-master/Python/intersection-of-two-linked-lists.py
# solution_class: Solution
# submission_id: 576d15c90b582b634fb6f5a4d4f6d30be2b43f4a
# seed: 3538126418

# Time:  O(m + n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA