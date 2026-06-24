# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-ways-to-make-the-sum
# source_path: LeetCode-Solutions-master/Python/the-number-of-ways-to-make-the-sum.py
# solution_class: Solution2
# submission_id: d093a5be2398e985626a860ee7cfd99c04ce6ce7
# seed: 801963829

# Time:  O(1)
# Space: O(1)

# math

class Solution2(object):
    def numberOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def count_1_2_6(n):
            # sum((n-6*i)//2+1 for i in xrange((n//6)+1))
            # = sum(((n//2)+1)-3*i for i in xrange((n//6)+1))
            return (n//2+1)*((n//6)-0+1)-3*((n//6)+0)*((n//6)-0+1)//2

        return reduce(lambda x, y: (x+count_1_2_6(n-4*y))%MOD, (i for i in xrange(min(n//4, 2)+1)), 0)