# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-fence
# source_path: LeetCode-Solutions-master/Python/paint-fence.py
# solution_class: Solution2
# submission_id: 6cae1fe385fdf162560318356c78f6d298576656
# seed: 3330383252

# Time:  O(n)
# Space: O(1)

class Solution2(object):
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
        ways = [0] * n
        ways[0] = k
        ways[1] = (k - 1) * ways[0] + k
        for i in xrange(2, n):
            ways[i] = (k - 1) * (ways[i - 1] + ways[i - 2])
        return ways[n - 1]