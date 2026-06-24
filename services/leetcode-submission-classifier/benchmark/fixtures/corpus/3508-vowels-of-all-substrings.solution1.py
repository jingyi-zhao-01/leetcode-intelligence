# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: vowels-of-all-substrings
# source_path: LeetCode-Solutions-master/Python/vowels-of-all-substrings.py
# solution_class: Solution
# submission_id: 02997e710159c5016e922d80b096dd4c5e0d86ac
# seed: 2320738703

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        VOWELS = set("aeiou")
        return sum((i-0+1) * ((len(word)-1)-i+1) for i, c in enumerate(word) if c in VOWELS)