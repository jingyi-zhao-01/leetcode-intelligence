# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-nesting-depth-of-two-valid-parentheses-strings
# source_path: LeetCode-Solutions-master/Python/maximum-nesting-depth-of-two-valid-parentheses-strings.py
# solution_class: Solution2
# submission_id: 00a23fc966e20bb282d9ab959e5af294bc86f598
# seed: 3408852436

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        A, B = 0, 0
        result = [0]*len(seq)
        for i, c in enumerate(seq):
            point = 1 if c == '(' else -1
            if (point == 1 and A <= B) or \
               (point == -1 and A >= B):
                A += point
            else:
                B += point
                result[i] = 1
        return result