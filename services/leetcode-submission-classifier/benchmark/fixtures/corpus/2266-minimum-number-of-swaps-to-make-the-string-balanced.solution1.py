# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-swaps-to-make-the-string-balanced
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-swaps-to-make-the-string-balanced.py
# solution_class: Solution
# submission_id: f6ff4f791a64e530bf9348482f2ae515ffaa4628
# seed: 2037600430

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = curr = 0
        for c in s:
            if c == ']':
                curr += 1
                result = max(result, curr)
            else:
                curr -= 1
        return (result+1)//2