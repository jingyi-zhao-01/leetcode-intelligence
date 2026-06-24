# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-manhattan-distance-after-k-changes
# source_path: LeetCode-Solutions-master/Python/maximum-manhattan-distance-after-k-changes.py
# solution_class: Solution
# submission_id: 53e9b1d928b7d422c50202ff16a640789c88e805
# seed: 3977037159

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = x = y = 0
        for i, c in enumerate(s, 1):
            if c == 'E':
                x += 1
            elif c == 'W':
                x -= 1
            elif c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            result = max(result, min(abs(x)+abs(y)+2*k, i))
        return result