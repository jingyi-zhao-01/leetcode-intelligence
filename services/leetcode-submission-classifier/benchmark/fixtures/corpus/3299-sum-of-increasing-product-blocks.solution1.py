# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-increasing-product-blocks
# source_path: LeetCode-Solutions-master/Python/sum-of-increasing-product-blocks.py
# solution_class: Solution
# submission_id: b1fec9c57042504be11c8915079178ac7224eb5f
# seed: 3001388772

# Time:  O(n^2)
# Space: O(n^2)

# simulation, math
MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
def lazy_init(n):
    while len(INV) <= n:  # lazy initialization
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)

def factorial(n):
    lazy_init(n)
    return FACT[n]

def inv_factorial(n):
    lazy_init(n)
    return INV_FACT[n]

class Solution(object):
    def sumOfBlocks(self, n):
        """
        :type n: int
        :rtype: int
        """        
        result, left = 0, 1
        for l in xrange(n):
            right = left+l
            result = (result+(factorial(right)*inv_factorial(left-1)))%MOD
            left = right+1
        return result