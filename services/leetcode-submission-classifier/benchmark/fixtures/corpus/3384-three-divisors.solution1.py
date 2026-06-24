# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: three-divisors
# source_path: LeetCode-Solutions-master/Python/three-divisors.py
# solution_class: Solution
# submission_id: f27bec5922b3d16db53fc059bc6cb93303fd7744
# seed: 3468295520

# Time:  O(sqrt(n))
# Space: O(1)

class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt = 0
        i = 1
        while i*i <= n and cnt <= 3:
            if n%i == 0:
                cnt += 1 if i*i == n else 2
            i += 1
        return cnt == 3