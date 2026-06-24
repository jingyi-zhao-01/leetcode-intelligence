# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-permutation
# source_path: LeetCode-Solutions-master/Python/find-permutation.py
# solution_class: Solution
# submission_id: bd645c01ee032c00e3a8d6d4a7592fd5476cb4dc
# seed: 929738127

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(s)+1):
            if i == len(s) or s[i] == 'I':
                result += range(i+1, len(result), -1)
        return result