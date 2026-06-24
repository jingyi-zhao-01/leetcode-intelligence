# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-all-as-appears-before-all-bs
# source_path: LeetCode-Solutions-master/Python/check-if-all-as-appears-before-all-bs.py
# solution_class: Solution
# submission_id: 695b69fb1373bed7bc9ce48a25688bcc088b749c
# seed: 2785150030

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "ba" not in s