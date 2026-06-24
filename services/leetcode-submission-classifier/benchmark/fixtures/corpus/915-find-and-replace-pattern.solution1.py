# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-and-replace-pattern
# source_path: LeetCode-Solutions-master/Python/find-and-replace-pattern.py
# solution_class: Solution
# submission_id: 75f519230471d03914e0cbf16287d0aec7400510
# seed: 2851485737

# Time:  O(n * l)
# Space: O(1)

import itertools

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            lookup = {}
            for x, y in itertools.izip(pattern, word):
                if lookup.setdefault(x, y) != y:
                    return False
            return len(set(lookup.values())) == len(lookup.values())

        return filter(match, words)