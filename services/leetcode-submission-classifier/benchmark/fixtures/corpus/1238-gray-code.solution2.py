# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: gray-code
# source_path: LeetCode-Solutions-master/Python/gray-code.py
# solution_class: Solution2
# submission_id: 1884a2ff9ef126cf7cc45e75fa679283ccf7206a
# seed: 2734766350

# Time:  O(2^n)
# Space: O(1)

class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i >> 1 ^ i for i in xrange(1 << n)]