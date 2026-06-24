# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number-iii
# source_path: LeetCode-Solutions-master/Python/single-number-iii.py
# solution_class: Solution3
# submission_id: 0b9328866b15518d801572b03b241e37344cd191
# seed: 3799839267

# Time:  O(n)
# Space: O(1)

import operator
import collections

class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [x[0] for x in sorted(collections.Counter(nums).items(), key=lambda i: i[1], reverse=False)[:2]]