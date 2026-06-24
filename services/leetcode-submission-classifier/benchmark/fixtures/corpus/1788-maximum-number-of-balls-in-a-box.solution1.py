# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-balls-in-a-box
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-balls-in-a-box.py
# solution_class: Solution
# submission_id: 5bff575150455172649d437aaabc1ecca0c66003
# seed: 765950099

# Time:  O(nlogm)
# Space: O(logm)

import collections
import itertools

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        count = collections.Counter()
        for i in xrange(lowLimit, highLimit+1):
            count[sum(itertools.imap(int, str(i)))] += 1
        return max(count.itervalues())