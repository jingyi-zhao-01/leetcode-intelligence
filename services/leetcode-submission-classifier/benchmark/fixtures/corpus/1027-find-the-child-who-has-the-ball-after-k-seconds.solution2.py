# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-child-who-has-the-ball-after-k-seconds
# source_path: LeetCode-Solutions-master/Python/find-the-child-who-has-the-ball-after-k-seconds.py
# solution_class: Solution2
# submission_id: e4ad60fbc8e57c5373282aa059c89e30d20df2a6
# seed: 1366287815

# Time:  O(1)
# Space: O(1)

# math

class Solution2(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        r = k%(2*(n-1))
        return r if r <= n-1 else (n-1)-(r-(n-1))