# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-binary-search-trees
# source_path: LeetCode-Solutions-master/Python/unique-binary-search-trees.py
# solution_class: Solution
# submission_id: d7b19c9be82c41a9792953ed7d903683aeb5daf8
# seed: 657559426

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        def combination(n, k):
            count = 1
            # C(n, k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
            for i in xrange(1, k + 1):
                count = count * (n - i + 1) / i
            return count

        return combination(2 * n, n) - combination(2 * n, n - 1)