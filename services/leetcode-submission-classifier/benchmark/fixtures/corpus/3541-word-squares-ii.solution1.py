# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-squares-ii
# source_path: LeetCode-Solutions-master/Python/word-squares-ii.py
# solution_class: Solution
# submission_id: 8e5c9bb9e6fd2ce9af71c331702860fd37356081
# seed: 3898425119

# Time:  O(n^4)
# Space: O(n)

import collections


# sort, brute force, hash table

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        words.sort()
        lookup = collections.defaultdict(list)
        for i, w in enumerate(words):
            lookup[w[0]].append(i)
            lookup[w[0], w[3]].append(i)
        result = []
        for i in xrange(len(words)):
            for j in lookup[words[i][0]]:
                if j == i:
                    continue
                for k in lookup[words[i][3]]:
                    if k in (i, j):
                        continue
                    for l in lookup[words[j][3], words[k][3]]:
                        if l in (i, j, k):
                            continue
                        result.append([words[i], words[j], words[k], words[l]])
        return result