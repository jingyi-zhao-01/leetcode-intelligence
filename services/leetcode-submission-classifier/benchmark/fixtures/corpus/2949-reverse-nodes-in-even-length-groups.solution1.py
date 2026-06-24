# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-nodes-in-even-length-groups
# source_path: LeetCode-Solutions-master/Python/reverse-nodes-in-even-length-groups.py
# solution_class: Solution
# submission_id: 82c0db536e29420cf178d86f01c8ac8cbaebab2b
# seed: 2863495752

# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, l = head, 2
        while prev.next:
            curr, cnt = prev, 0
            for _ in xrange(l):
                if not curr.next:
                    break
                cnt += 1
                curr = curr.next
            l += 1
            if cnt%2:
                prev = curr
                continue
            curr, last = prev.next, None
            for _ in xrange(cnt):
                curr.next, curr, last = last, curr.next, curr
            prev.next.next, prev.next, prev = curr, last, prev.next
        return head