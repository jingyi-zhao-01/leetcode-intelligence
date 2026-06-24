# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: redistribute-characters-to-make-all-strings-equal
# source_path: LeetCode-Solutions-master/Python/redistribute-characters-to-make-all-strings-equal.py
# solution_class: Solution
# submission_id: ed59e648c728ac939214c95f06c9eb446d689ed6
# seed: 4083111221

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        cnt = collections.defaultdict(int)
        for w in words:
            for c in w:
                cnt[c] += 1
        return all(v%len(words) == 0 for v in cnt.itervalues())