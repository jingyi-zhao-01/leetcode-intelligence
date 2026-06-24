# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-resultant-array-after-removing-anagrams
# source_path: LeetCode-Solutions-master/Python/find-resultant-array-after-removing-anagrams.py
# solution_class: Solution3
# submission_id: c801a3308f4477c3f000e7bce5c3105ff77ab5e0
# seed: 2884252631

# Time:  O(n * l)
# Space: O(1)

import collections


# freq table

class Solution3(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [words[i] for i in xrange(len(words)) if i == 0 or sorted(words[i-1]) != sorted(words[i])]