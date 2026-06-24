# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-nodes-from-linked-list
# source_path: LeetCode-Solutions-master/Python/remove-nodes-from-linked-list.py
# solution_class: Solution
# submission_id: 1ec159ce7d69b97a911d795e5a4c32cb53347ffa
# seed: 730500079

# Time:  O(n)
# Space: O(n)

class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


# mono stack

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stk = []
        while head:
            while stk and stk[-1].val < head.val:
                stk.pop()
            if stk:
                stk[-1].next = head
            stk.append(head)
            head = head.next
        return stk[0]