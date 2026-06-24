# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-strings-by-separator
# source_path: LeetCode-Solutions-master/Python/split-strings-by-separator.py
# solution_class: Solution
# submission_id: 825bb4a8661366c8c1f97ba23560be477d3f3957
# seed: 4276043832

# Time:  O(n * l)
# Space: O(l)

# string

class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        return [w for word in words for w in word.split(separator) if w]