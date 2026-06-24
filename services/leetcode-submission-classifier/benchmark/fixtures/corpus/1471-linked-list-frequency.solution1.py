# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-frequency
# source_path: LeetCode-Solutions-master/Python/linked-list-frequency.py
# solution_class: Solution
# submission_id: 91b7042cb86b62df0a7ee818d78215e8f0c285a6
# seed: 542215853

# Time:  O(n)
# Space: O(1)

# linked list

class Solution(object):
    def frequenciesOfElements(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = dummy = ListNode(0)
        cnt = 0
        while head:
            cnt += 1
            if not head.next or head.next.val != head.val:
                curr.next = ListNode(cnt)
                curr = curr.next
                cnt = 0
            head = head.next
        return dummy.next