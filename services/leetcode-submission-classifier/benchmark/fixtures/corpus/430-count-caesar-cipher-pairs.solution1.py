# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-caesar-cipher-pairs
# source_path: LeetCode-Solutions-master/Python/count-caesar-cipher-pairs.py
# solution_class: Solution
# submission_id: ccddba64f00b44b8737c4938cd220ddcc9927116
# seed: 1936524922

# Time:  O(n * m)
# Space: O(n * m)

import collections


# freq table

class Solution(object):
    def countPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def f(s):
            return "".join(chr(ord('a')+((ord(x)-ord(s[0]))%26)) for x in s)

        result = 0
        cnt = collections.defaultdict(int)
        for w in words:
            s = f(w)
            result += cnt[s]
            cnt[s] += 1
        return result