# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: odd-string-difference
# source_path: LeetCode-Solutions-master/Python/odd-string-difference.py
# solution_class: Solution
# submission_id: 087f570cc17eab0011b7c14cbd7a83cc52ef670b
# seed: 846050632

# Time:  O(m * n), m is the number of words, n is the length of each word
# Space: O(1)

import collections


# freq table

class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in xrange(len(words[0])-1):
            lookup = collections.defaultdict(list)
            for j, w in enumerate(words):
                if len(lookup[ord(w[i+1])-ord(w[i])]) < 2:
                    lookup[ord(w[i+1])-ord(w[i])].append(j)
            if len(lookup) == 2:
                return next(words[l[0]] for l in lookup.itervalues() if len(l) == 1)