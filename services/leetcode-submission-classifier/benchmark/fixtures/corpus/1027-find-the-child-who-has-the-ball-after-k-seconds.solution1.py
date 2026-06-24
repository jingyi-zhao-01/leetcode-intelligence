# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-child-who-has-the-ball-after-k-seconds
# source_path: LeetCode-Solutions-master/Python/find-the-child-who-has-the-ball-after-k-seconds.py
# solution_class: Solution
# submission_id: b8e028c944c2aa9d5e13b00f1f045dd2c4c40c1a
# seed: 1179702136

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        q, r = divmod(k, n-1)
        return r if q&1 == 0 else (n-1)-r