# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-prefix-and-suffix-pairs-i
# source_path: LeetCode-Solutions-master/Python/count-prefix-and-suffix-pairs-i.py
# solution_class: Solution2
# submission_id: 9463ad64ed4fbf62f7d83b4b229d7b1004a1c44b
# seed: 4124884015

# Time:  O(n * l)
# Space: O(t)

import collections


# trie

class Solution2(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def check(i, j):
            return words[j].startswith(words[i]) and words[j].endswith(words[i])
    
        return sum(check(i, j) for i in xrange(len(words)) for j in xrange(i+1, len(words)))