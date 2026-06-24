# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-possible-number-by-binary-concatenation
# source_path: LeetCode-Solutions-master/Python/maximum-possible-number-by-binary-concatenation.py
# solution_class: Solution2
# submission_id: 4bd3f5db3eedb3a5aa7e223c4bf8aef28de1ea2e
# seed: 983568253

# Time:  O(n * logr * logn)
# Space: O(nlogr)

# sort

class Solution2(object):
    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(int("".join(x), 2) for x in itertools.permutations(map(lambda x: bin(x)[2:], nums)))