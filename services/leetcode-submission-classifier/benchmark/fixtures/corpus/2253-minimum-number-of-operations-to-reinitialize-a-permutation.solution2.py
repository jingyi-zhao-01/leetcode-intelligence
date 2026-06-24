# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-reinitialize-a-permutation
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-reinitialize-a-permutation.py
# solution_class: Solution2
# submission_id: bb96e797d55f46710a59cd2eb0380afede1ce7a8
# seed: 2029501074

# Time:  O(sqrt(n))
# Space: O(sqrt(n))

class Solution2(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        result, i = 0, 1
        while not result or i != 1:
            i = (i*2)%(n-1)
            result += 1
        return result