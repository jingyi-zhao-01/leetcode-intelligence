# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-amount-of-time-to-collect-garbage
# source_path: LeetCode-Solutions-master/Python/minimum-amount-of-time-to-collect-garbage.py
# solution_class: Solution
# submission_id: d2e8de515becf2a63413e925651d33942cce95bd
# seed: 3230117012

# Time:  O(n * l), l = max(len(g) for g in garbage) = O(10)
# Space: O(1)

# simulation, prefix sum

class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        result = 0
        lookup = {}
        for i in xrange(len(garbage)):
            for c in garbage[i]:
                lookup[c] = i
            if i+1 < len(travel):
                travel[i+1] += travel[i]
            result += len(garbage[i])
        result += sum(travel[v-1] for _, v in lookup.iteritems() if v-1 >= 0)
        return result