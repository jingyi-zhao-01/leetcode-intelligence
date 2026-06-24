# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-resultant-array-after-removing-anagrams
# source_path: LeetCode-Solutions-master/Python/find-resultant-array-after-removing-anagrams.py
# solution_class: Solution
# submission_id: be00bf5074d948e000bba58668ebc952cda455b5
# seed: 3786609623

# Time:  O(n * l)
# Space: O(1)

import collections


# freq table

class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        prev = None
        for x in words:
            cnt = collections.Counter(x)
            if prev and prev == cnt:
                continue
            prev = cnt
            result.append(x)
        return result