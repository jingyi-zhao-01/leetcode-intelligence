# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-amount-of-time-to-collect-garbage
# source_path: LeetCode-Solutions-master/Python/minimum-amount-of-time-to-collect-garbage.py
# solution_class: Solution2
# submission_id: ad63c3952fa2d5ecf797c31565a117b282847507
# seed: 1593227182

# Time:  O(n * l), l = max(len(g) for g in garbage) = O(10)
# Space: O(1)

# simulation, prefix sum

class Solution2(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        result = 0
        for t in 'MPG':
            curr = 0
            for i in xrange(len(garbage)):
                cnt = garbage[i].count(t) 
                if cnt:
                    result += curr+cnt
                    curr = 0
                if i < len(travel):
                    curr += travel[i]
        return result