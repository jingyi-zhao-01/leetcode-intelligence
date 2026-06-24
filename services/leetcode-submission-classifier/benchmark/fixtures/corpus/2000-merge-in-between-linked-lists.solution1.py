# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-in-between-linked-lists
# source_path: LeetCode-Solutions-master/Python/merge-in-between-linked-lists.py
# solution_class: Solution
# submission_id: e3f7ffe71d7da31b6124afac546aa6b411793a70
# seed: 759237983

# Time:  O(m + n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        pass

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        prev_first, last = None, list1
        for i in xrange(b):
            if i == a-1:
                prev_first = last
            last = last.next
        prev_first.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = last.next
        last.next = None
        return list1