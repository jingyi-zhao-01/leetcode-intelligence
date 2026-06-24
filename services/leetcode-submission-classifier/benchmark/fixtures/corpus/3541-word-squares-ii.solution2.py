# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-squares-ii
# source_path: LeetCode-Solutions-master/Python/word-squares-ii.py
# solution_class: Solution2
# submission_id: 75f887a41785f950050dae02a62fb4cc2b3cb2b6
# seed: 1333024425

# Time:  O(n^4)
# Space: O(n)

import collections


# sort, brute force, hash table

class Solution2(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        words.sort()
        result = []
        for i in xrange(len(words)):
            for j in xrange(len(words)):
                if j == i or words[j][0] != words[i][0]:
                    continue
                for k in xrange(len(words)):
                    if k in (i, j) or words[k][0] != words[i][3]:
                        continue
                    for l in xrange(len(words)):
                        if l in (i, j, k) or words[l][0] != words[j][3] or words[l][3] != words[k][3]:
                            continue
                        result.append([words[i], words[j], words[k], words[l]])
        return result