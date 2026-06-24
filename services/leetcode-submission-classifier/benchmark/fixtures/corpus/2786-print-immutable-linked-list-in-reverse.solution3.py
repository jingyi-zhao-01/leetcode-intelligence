# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: print-immutable-linked-list-in-reverse
# source_path: LeetCode-Solutions-master/Python/print-immutable-linked-list-in-reverse.py
# solution_class: Solution3
# submission_id: 8e19d1b2c7ab7592b4064a2b1c5f44814afa7885
# seed: 2810451476

# Time:  O(n)
# Space: O(sqrt(n))

import math

class Solution3(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        tail = None
        while head != tail:
            curr = head
            while curr.getNext() != tail:
                curr = curr.getNext()
            curr.printValue()
            tail = curr