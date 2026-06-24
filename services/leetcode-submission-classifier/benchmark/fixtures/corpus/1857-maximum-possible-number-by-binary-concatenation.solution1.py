# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-possible-number-by-binary-concatenation
# source_path: LeetCode-Solutions-master/Python/maximum-possible-number-by-binary-concatenation.py
# solution_class: Solution
# submission_id: 0a992f648da2ab7eaed778747fb1a1999d1ecf8d
# seed: 3238255269

# Time:  O(n * logr * logn)
# Space: O(nlogr)

# sort

class Solution(object):
    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int("".join(sorted(map(lambda x: bin(x)[2:], nums), cmp=lambda x, y: (x+y > y+x)-(x+y < y+x), reverse=True)), 2)