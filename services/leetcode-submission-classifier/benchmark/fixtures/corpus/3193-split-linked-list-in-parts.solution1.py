# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-linked-list-in-parts
# source_path: LeetCode-Solutions-master/Python/split-linked-list-in-parts.py
# solution_class: Solution
# submission_id: aaffb33f4be4bf0270a9eb7b408efc13cfdf11a9
# seed: 3845217994

# Time:  O(n + k)
# Space: O(1)

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = 0
        curr = root
        while curr:
            curr = curr.next
            n += 1
        width, remainder = divmod(n, k)

        result = []
        curr = root
        for i in xrange(k):
            head = curr
            for j in xrange(width-1+int(i < remainder)):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            result.append(head)
        return result