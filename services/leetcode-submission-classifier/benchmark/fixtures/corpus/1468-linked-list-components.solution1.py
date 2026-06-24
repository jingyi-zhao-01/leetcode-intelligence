# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-components
# source_path: LeetCode-Solutions-master/Python/linked-list-components.py
# solution_class: Solution
# submission_id: ad2880db516ea82653e78f5b3c2a79a97a987cd4
# seed: 789551273

# Time:  O(m + n), m is the number of G, n is the number of nodes
# Space: O(m)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        lookup = set(G)
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        result = 0
        while curr and curr.next:
            if curr.val not in lookup and curr.next.val in lookup:
                result += 1
            curr = curr.next
        return result