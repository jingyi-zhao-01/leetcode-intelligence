# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: print-immutable-linked-list-in-reverse
# source_path: LeetCode-Solutions-master/Python/print-immutable-linked-list-in-reverse.py
# solution_class: Solution2
# submission_id: 421b73c165daf57dbb9739ba9656f1e42e7a4259
# seed: 881077362

# Time:  O(n)
# Space: O(sqrt(n))

import math

class Solution2(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.getNext()
        for node in reversed(nodes):
            node.printValue()