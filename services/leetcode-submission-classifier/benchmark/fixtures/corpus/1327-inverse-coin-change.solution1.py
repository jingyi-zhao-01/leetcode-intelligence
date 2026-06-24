# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: inverse-coin-change
# source_path: LeetCode-Solutions-master/Python/inverse-coin-change.py
# solution_class: Solution
# submission_id: da2fdf8a3ea422c9a69153cc4b5f6a5339855c5c
# seed: 830150301

# Time:  O(n^2)
# Space: O(1)

# dp

class Solution(object):
    def findCoins(self, numWays):
        """
        :type numWays: List[int]
        :rtype: List[int]
        """
        result = []
        for i in xrange(1, len(numWays)+1):
            if numWays[i-1] == 1:
                result.append(i)
                for j in reversed(xrange(i, len(numWays)+1)):
                    numWays[j-1] -= numWays[(j-i)-1] if (j-i)-1 >= 0 else 1
            if numWays[i-1]:
                return []
        return result