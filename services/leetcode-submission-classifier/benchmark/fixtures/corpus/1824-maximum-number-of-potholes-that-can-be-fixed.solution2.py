# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-potholes-that-can-be-fixed
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-potholes-that-can-be-fixed.py
# solution_class: Solution2
# submission_id: 4ff5eac50afeec2a2e4e7d643027f2b4425a6838
# seed: 3073097056

# Time:  O(n)
# Space: O(n)

# counting sort, greedy

class Solution2(object):
    def maxPotholes(self, road, budget):
        """
        :type road: str
        :type budget: int
        :rtype: int
        """
        ls = []
        l = 0
        for i in xrange(len(road)):
            l += 1
            if i+1 == len(road) or road[i+1] != road[i]:
                if road[i] == 'x':
                    ls.append(l)
                l = 0
        ls.sort()
        result = 0
        for l in reversed(ls):
            c = min(l+1, budget)
            if c-1 <= 0:
                break
            result += c-1
            budget -= c
        return result