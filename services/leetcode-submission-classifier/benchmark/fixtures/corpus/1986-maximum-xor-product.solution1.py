# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-product
# source_path: LeetCode-Solutions-master/Python/maximum-xor-product.py
# solution_class: Solution
# submission_id: f254f17cdd8023b9b03294cce2afc4828e9d3274
# seed: 3733578427

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maximumXorProduct(self, a, b, n):
        """
        :type a: int
        :type b: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        for i in reversed(xrange(n)):
            base = 1<<i
            if min(a, b)&base == 0:
                a, b = a^base, b^base
        return (a%MOD)*(b%MOD)%MOD