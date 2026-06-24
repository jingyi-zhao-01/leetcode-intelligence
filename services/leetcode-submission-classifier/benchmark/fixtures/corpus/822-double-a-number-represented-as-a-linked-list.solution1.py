# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: double-a-number-represented-as-a-linked-list
# source_path: LeetCode-Solutions-master/Python/double-a-number-represented-as-a-linked-list.py
# solution_class: Solution
# submission_id: 7cdd328e58d8df1c55ffac0821b7e6561f0d9252
# seed: 2342624024

# Time:  O(n)
# Space: O(1)

# linked list

class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.val >= 5:
            head = ListNode(0, head)
        curr = head
        while curr:
            curr.val = (curr.val*2)%10
            if curr.next and curr.next.val >= 5:
                curr.val += 1
            curr = curr.next
        return head