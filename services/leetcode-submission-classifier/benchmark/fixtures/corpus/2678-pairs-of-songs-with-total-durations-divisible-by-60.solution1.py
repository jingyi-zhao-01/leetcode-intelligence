# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pairs-of-songs-with-total-durations-divisible-by-60
# source_path: LeetCode-Solutions-master/Python/pairs-of-songs-with-total-durations-divisible-by-60.py
# solution_class: Solution
# submission_id: 333f74fb42b3ed39a07f8ded2ee5d11350750cbd
# seed: 272844346

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        result = 0
        count = collections.Counter()
        for t in time:
            result += count[-t%60]
            count[t%60] += 1
        return result