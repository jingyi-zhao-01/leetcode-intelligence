# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-buy-pens-and-pencils
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-buy-pens-and-pencils.py
# solution_class: Solution2
# submission_id: 15d3d22405ca08c35da30d64a5d02f332e3cfd23
# seed: 3817414376

# Time:  O(min(t / c1, c2 / g)) = O(sqrt(t)), c1 = max(cost1, cost2)
#                                           , c2 = min(cost1, cost2)
#                                           ,  g = gcd(c1, c2)
# Space: O(1)

# math

class Solution2(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        return sum((total-i*cost1)//cost2+1 for i in xrange(total//cost1+1))