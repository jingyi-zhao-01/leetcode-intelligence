# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-if-two-strings-are-close
# source_path: LeetCode-Solutions-master/Python/determine-if-two-strings-are-close.py
# solution_class: Solution
# submission_id: bc243fd6c72f7c113ad33272f166882a994b5cec
# seed: 1000680480

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False 
        
        cnt1, cnt2 = collections.Counter(word1), collections.Counter(word2)   # Reuse of keys
        return set(cnt1.iterkeys()) == set(cnt2.iterkeys()) and \
               collections.Counter(cnt1.itervalues()) == collections.Counter(cnt2.itervalues())