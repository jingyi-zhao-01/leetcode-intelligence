# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: detect-capital
# source_path: LeetCode-Solutions-master/Python/detect-capital.py
# solution_class: Solution
# submission_id: 363f0784e18464b54595f1988954e5499806433d
# seed: 3645524725

# Time:  O(l)
# Space: O(1)

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()