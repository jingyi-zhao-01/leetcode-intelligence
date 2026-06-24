# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-ways-to-make-the-sum
# source_path: LeetCode-Solutions-master/Python/the-number-of-ways-to-make-the-sum.py
# solution_class: Solution3
# submission_id: b0f8b9d50539e6f2153ce2857cbba845cebb12ee
# seed: 417991198

# Time:  O(1)
# Space: O(1)

# math

class Solution3(object):
    def numberOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def count_1_2(n):
            return n//2+1
    
        def count_1_2_6(n):
            return sum(count_1_2(n-6*i) for i in xrange((n//6)+1))

        return reduce(lambda x, y: (x+count_1_2_6(n-4*y))%MOD, (i for i in xrange(min(n//4, 2)+1)), 0)