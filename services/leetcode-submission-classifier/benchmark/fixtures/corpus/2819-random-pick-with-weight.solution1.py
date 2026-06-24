# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: random-pick-with-weight
# source_path: LeetCode-Solutions-master/Python/random-pick-with-weight.py
# solution_class: Solution
# submission_id: bdd77d07a6dccb07cd0e9f660c5addedc67c4b03
# seed: 514706724

# Time:  ctor: O(n)
#        pickIndex: O(logn)
# Space: O(n)

import random
import bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.__prefix_sum = list(w)
        for i in xrange(1, len(w)):
            self.__prefix_sum[i] += self.__prefix_sum[i-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(0, self.__prefix_sum[-1]-1)
        return bisect.bisect_right(self.__prefix_sum, target)