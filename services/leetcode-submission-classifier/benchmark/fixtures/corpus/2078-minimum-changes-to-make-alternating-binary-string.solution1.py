# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-changes-to-make-alternating-binary-string
# source_path: LeetCode-Solutions-master/Python/minimum-changes-to-make-alternating-binary-string.py
# solution_class: Solution
# submission_id: cb229151988aae24e63264ec1c1a3f5970117e42
# seed: 368054186

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = sum(int(c) == i%2 for i, c in enumerate(s))
        return min(cnt, len(s)-cnt)