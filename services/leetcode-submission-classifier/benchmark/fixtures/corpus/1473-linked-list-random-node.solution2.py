# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-random-node
# source_path: LeetCode-Solutions-master/Python/linked-list-random-node.py
# solution_class: Solution2
# submission_id: c5e99a93dc1a6a4491d6da3fd2c3b2408cb94f42
# seed: 741224628

# Time:  ctor:      O(1)
#        getRandom: O(n)
# Space: O(1)

from random import randint


# if the length is unknown without using extra space

class Solution2(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.__lookup = []
        while head:
            self.__lookup.append(head.val)
            head = head.next
        

    def getRandom(self):
        """
        :rtype: int
        """
        return self.__lookup[randint(0, len(self.__lookup)-1)]