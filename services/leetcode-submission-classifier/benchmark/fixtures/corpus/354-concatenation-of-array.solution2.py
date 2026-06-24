# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: concatenation-of-array
# source_path: LeetCode-Solutions-master/Python/concatenation-of-array.py
# solution_class: Solution2
# submission_id: bc156e1408d5a1ca1c4253af63ecb21b1568a902
# seed: 1946518390

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums+nums