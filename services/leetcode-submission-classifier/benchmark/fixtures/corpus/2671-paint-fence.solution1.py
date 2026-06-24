# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-fence
# source_path: LeetCode-Solutions-master/Python/paint-fence.py
# solution_class: Solution
# submission_id: 16865ece13552278ecd1fb5b512e8010f1cf23ba
# seed: 142475937

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        ways = [0] * 3
        ways[0] = k
        ways[1] = (k - 1) * ways[0] + k
        for i in xrange(2, n):
            ways[i % 3] = (k - 1) * (ways[(i - 1) % 3] + ways[(i - 2) % 3])
        return ways[(n - 1) % 3]