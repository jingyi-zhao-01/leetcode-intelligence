# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-levels-to-gain-more-points
# source_path: LeetCode-Solutions-master/Python/minimum-levels-to-gain-more-points.py
# solution_class: Solution
# submission_id: 73c694af13f0e55c682df8d31fb5fa80c3e0118c
# seed: 2518044197

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution(object):
    def minimumLevels(self, possible):
        """
        :type possible: List[int]
        :rtype: int
        """
        prefix = [0]*(len(possible)+1)
        for i in xrange(len(possible)):
            prefix[i+1] = prefix[i]+(+1 if possible[i] else -1)
        return next((i+1 for i in xrange(len(possible)-1) if prefix[i+1] > prefix[-1]-prefix[i+1]), -1)