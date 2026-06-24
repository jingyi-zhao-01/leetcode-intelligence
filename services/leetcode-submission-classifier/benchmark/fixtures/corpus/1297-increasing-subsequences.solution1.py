# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: increasing-subsequences
# source_path: LeetCode-Solutions-master/Python/increasing-subsequences.py
# solution_class: Solution
# submission_id: 48ecaa8008568badd4884ab8fd37405de65e8073
# seed: 3097496311

# Time:  O(n * 2^n)
# Space: O(n), longest possible path in tree, which is if all numbers are increasing.

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def findSubsequencesHelper(nums, pos, seq, result):
            if len(seq) >= 2:
                result.append(list(seq))
            lookup = set()
            for i in xrange(pos, len(nums)):
                if (not seq or nums[i] >= seq[-1]) and \
                   nums[i] not in lookup:
                    lookup.add(nums[i])
                    seq.append(nums[i])
                    findSubsequencesHelper(nums, i+1, seq, result)
                    seq.pop()

        result, seq = [], []
        findSubsequencesHelper(nums, 0, seq, result)
        return result