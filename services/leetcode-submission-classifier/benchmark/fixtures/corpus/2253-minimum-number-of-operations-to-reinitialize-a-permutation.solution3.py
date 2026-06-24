# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-reinitialize-a-permutation
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-reinitialize-a-permutation.py
# solution_class: Solution3
# submission_id: bb92b32e914a07b304219feae989db35cb0f4284
# seed: 2087204921

# Time:  O(sqrt(n))
# Space: O(sqrt(n))

class Solution3(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        result, i = 0, 1
        while not result or i != 1:  # find cycle length
            i = (i//2 if not i%2 else n//2+(i-1)//2)
            result += 1
        return result