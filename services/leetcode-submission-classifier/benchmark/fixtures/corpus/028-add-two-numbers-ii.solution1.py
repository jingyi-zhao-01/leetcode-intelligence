# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-two-numbers-ii
# source_path: LeetCode-Solutions-master/Python/add-two-numbers-ii.py
# solution_class: Solution
# submission_id: d884113ec07f5b564296d5e9a1eecfd0c5d1d2f3
# seed: 2088757704

# Time:  O(m + n)
# Space: O(m + n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next

        prev, head = None, None
        sum = 0
        while stk1 or stk2:
            sum /= 10
            if stk1:
                sum += stk1.pop()
            if stk2:
                sum += stk2.pop()

            head = ListNode(sum % 10)
            head.next = prev
            prev = head

        if sum >= 10:
            head = ListNode(sum / 10)
            head.next = prev

        return head