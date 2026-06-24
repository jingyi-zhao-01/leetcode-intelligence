# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: words-within-two-edits-of-dictionary
# source_path: LeetCode-Solutions-master/Python/words-within-two-edits-of-dictionary.py
# solution_class: Solution2
# submission_id: 01d099fc02a2705cc1e4cbebaae0a296857d3004
# seed: 2150907151

# Time:  O(25 * l * (n + q))
# Space: O(25 * l * n)

import string


# hash

class Solution2(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        return [q for q in queries if any(sum(c1 != c2 for c1, c2 in itertools.izip(q, d)) <= 2 for d in dictionary)]