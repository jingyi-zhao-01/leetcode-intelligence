# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-integer-to-the-sum-of-two-no-zero-integers
# source_path: LeetCode-Solutions-master/Python/convert-integer-to-the-sum-of-two-no-zero-integers.py
# solution_class: Solution2
# submission_id: be0d367bceb023a7af63041a76028d6ec25bb540
# seed: 1053682228

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return next([a, n-a] for a in xrange(1, n) if '0' not in '{}{}'.format(a, n-a))