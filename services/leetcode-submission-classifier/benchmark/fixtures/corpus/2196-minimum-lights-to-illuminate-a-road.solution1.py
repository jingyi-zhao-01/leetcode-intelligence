# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-lights-to-illuminate-a-road
# source_path: LeetCode-Solutions-master/Python/minimum-lights-to-illuminate-a-road.py
# solution_class: Solution
# submission_id: 0c81b4bb399cd39675a94fd94be36f50a445e8a1
# seed: 438462550

# Time:  O(n)
# Space: O(n)

# difference array, greedy

class Solution(object):
    def minLights(self, lights):
        """
        :type lights: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
        
        diff = [0]*(len(lights)+1)
        for i in xrange(len(lights)):
            if not lights[i]:
                continue
            diff[max(i-lights[i], 0)] += 1
            diff[min(i+lights[i], len(lights)-1)+1] -= 1
        result = curr = cnt = 0
        for i in xrange(len(diff)):
            curr += diff[i]
            if i+1 == len(diff) or curr:
                result += ceil_divide(cnt, 3)
                cnt = 0
            else:
                cnt += 1
        return result