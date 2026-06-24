# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: copy-list-with-random-pointer
# source_path: LeetCode-Solutions-master/Python/copy-list-with-random-pointer.py
# solution_class: Solution3
# submission_id: d7bc3a2900ad8a0d94b8340d4cf0af17ac7c79d4
# seed: 3099356493

# Time:  O(n)
# Space: O(1)

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution3(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        clone = defaultdict(lambda: Node(0))
        clone[None] = None
        cur = head

        while cur:
            clone[cur].val = cur.val
            clone[cur].next = clone[cur.next]
            clone[cur].random = clone[cur.random]
            cur = cur.next

        return clone[head]