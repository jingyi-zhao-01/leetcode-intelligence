# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-words-containing-character
# source_path: LeetCode-Solutions-master/Python/find-words-containing-character.py
# solution_class: Solution
# submission_id: c1e152219bd96dea00eccf45c1fcd9fe66845049
# seed: 3046796851

# Time:  O(n * l)
# Space: O(1)

# string

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        return [i for i, w in enumerate(words) if x in w]