# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-random-node
# source_path: LeetCode-Solutions-master/Python/linked-list-random-node.py
# solution_class: Solution
# submission_id: 6ff970571925c9a7349ff337f6b8c33a81b13a4c
# seed: 3676537820

# Time:  ctor:      O(1)
#        getRandom: O(n)
# Space: O(1)

from random import randint


# if the length is unknown without using extra space

class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.__head = head


    # Proof of Reservoir Sampling:
    # https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling
    def getRandom(self):
        """
        :rtype: int
        """
        reservoir = -1
        curr, n = self.__head, 0
        while curr:
            reservoir = curr.val if randint(1, n+1) == 1 else reservoir
            curr, n = curr.next, n+1
        return reservoir