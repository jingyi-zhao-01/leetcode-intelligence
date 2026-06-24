# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-duplicates-from-sorted-list
# source_path: LeetCode-Solutions-master/Python/remove-duplicates-from-sorted-list.py
# solution_class: Solution
# submission_id: ef2c6758354a8c9eec851ba4427e696cd028eae4
# seed: 773883978

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            runner = cur.next
            while runner and runner.val == cur.val:
                runner = runner.next
            cur.next = runner
            cur = runner
        return head

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        if head.next:
            if head.val == head.next.val:
                head = self.deleteDuplicates2(head.next)
            else:
                head.next = self.deleteDuplicates2(head.next)
        return head