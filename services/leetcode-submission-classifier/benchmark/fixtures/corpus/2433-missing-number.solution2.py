# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: missing-number
# source_path: LeetCode-Solutions-master/Python/missing-number.py
# solution_class: Solution2
# submission_id: f8dfbfc707df104dbc4a3e18f5badaf2e0596453
# seed: 4015669534

# Time:  O(n)
# Space: O(1)

import operator

class Solution2(object):
    def missingNumber(self, nums):
        return sum(xrange(len(nums)+1)) - sum(nums)