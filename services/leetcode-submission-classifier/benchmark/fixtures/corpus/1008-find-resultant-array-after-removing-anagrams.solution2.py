# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-resultant-array-after-removing-anagrams
# source_path: LeetCode-Solutions-master/Python/find-resultant-array-after-removing-anagrams.py
# solution_class: Solution2
# submission_id: a6f18fba933c0844bc0767f70ad40e33dd056709
# seed: 1207968786

# Time:  O(n * l)
# Space: O(1)

import collections


# freq table

class Solution2(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        prev = None
        for x in words:
            s = sorted(x)
            if prev and prev == s:
                continue
            prev = s
            result.append(x)
        return result