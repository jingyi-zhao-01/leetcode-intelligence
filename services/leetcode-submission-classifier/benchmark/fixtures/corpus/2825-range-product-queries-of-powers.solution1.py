# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: range-product-queries-of-powers
# source_path: LeetCode-Solutions-master/Python/range-product-queries-of-powers.py
# solution_class: Solution
# submission_id: f1b2515924eb8801dae0a0d4aaa964365c61f696
# seed: 2394679950

# Time:  O(logn + qlogr), r = MOD
# Space: O(logn)

# prefix sum

class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9+7
        prefix = [0]
        i = 0
        while (1<<i) <= n:
            if n&(1<<i):
                prefix.append(prefix[-1]+i)
            i += 1
        return [pow(2, prefix[r+1]-prefix[l], MOD) for l, r in queries]