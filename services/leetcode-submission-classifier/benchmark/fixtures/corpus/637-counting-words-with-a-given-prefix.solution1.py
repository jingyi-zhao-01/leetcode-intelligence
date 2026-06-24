# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: counting-words-with-a-given-prefix
# source_path: LeetCode-Solutions-master/Python/counting-words-with-a-given-prefix.py
# solution_class: Solution
# submission_id: d444fbe72c490e20779f7fcc2a5d7a6cfcc8987d
# seed: 1052097215

# Time:  O(n * p)
# Space: O(1)

# string

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return sum(x.startswith(pref) for x in words)