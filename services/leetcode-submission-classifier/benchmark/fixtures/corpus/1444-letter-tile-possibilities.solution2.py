# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: letter-tile-possibilities
# source_path: LeetCode-Solutions-master/Python/letter-tile-possibilities.py
# solution_class: Solution2
# submission_id: e8e3f5bb74189efe81c2a30b9b5618d956607400
# seed: 3009005233

# Time:  O(n^2)
# Space: O(n)

import collections

class Solution2(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def backtracking(counter):
            total = 0
            for k, v in counter.iteritems():
                if not v:
                    continue
                counter[k] -= 1
                total += 1+backtracking(counter)
                counter[k] += 1
            return total

        return backtracking(collections.Counter(tiles))