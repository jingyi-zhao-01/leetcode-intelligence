# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: can-you-eat-your-favorite-candy-on-your-favorite-day
# source_path: LeetCode-Solutions-master/Python/can-you-eat-your-favorite-candy-on-your-favorite-day.py
# solution_class: Solution
# submission_id: ab3baad1def1975310fb4d9bc093dade6997017a
# seed: 2615444052

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prefix = [0]*(len(candiesCount)+1)
        for i, c in enumerate(candiesCount):
            prefix[i+1] = prefix[i]+c
        return [prefix[t]//c < d+1 <= prefix[t+1]//1 for t, d, c in queries]