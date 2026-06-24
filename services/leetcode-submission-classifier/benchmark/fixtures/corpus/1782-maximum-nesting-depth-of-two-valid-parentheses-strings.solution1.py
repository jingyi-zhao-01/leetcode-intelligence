# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-nesting-depth-of-two-valid-parentheses-strings
# source_path: LeetCode-Solutions-master/Python/maximum-nesting-depth-of-two-valid-parentheses-strings.py
# solution_class: Solution
# submission_id: f435868e4e58884b5b2c0c44dcff9f5c32f1c865
# seed: 3759921353

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        return [(i & 1) ^ (seq[i] == '(') for i, c in enumerate(seq)]