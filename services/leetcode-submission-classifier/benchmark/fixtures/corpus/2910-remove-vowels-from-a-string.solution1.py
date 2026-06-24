# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-vowels-from-a-string
# source_path: LeetCode-Solutions-master/Python/remove-vowels-from-a-string.py
# solution_class: Solution
# submission_id: 49a69e7fb51d37312b1f2631160f10cdb9941b28
# seed: 2340587707

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        lookup = set("aeiou")
        return "".join(c for c in S if c not in lookup)