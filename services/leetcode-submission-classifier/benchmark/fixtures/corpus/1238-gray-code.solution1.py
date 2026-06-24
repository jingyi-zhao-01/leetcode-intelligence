# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: gray-code
# source_path: LeetCode-Solutions-master/Python/gray-code.py
# solution_class: Solution
# submission_id: f7bfff08f8b14e2aa959881bf65c43a0dae6d915
# seed: 3289146586

# Time:  O(2^n)
# Space: O(1)

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in xrange(n):
            for n in reversed(result):
                result.append(1 << i | n)
        return result