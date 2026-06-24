# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-two-digits
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-two-digits.py
# solution_class: Solution
# submission_id: 1ef9530aef2ade0ce4ba455d04c8a8facfce30ba
# seed: 3879004561

# Time:  O(d + 10)
# Space: O(10)

# freq table, greedy

class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        MAX_COUNT = 2
        def count(n):
            cnt = [0]*10
            while n:
                n, r = divmod(n, 10)
                cnt[r] += 1
            return cnt

        cnt = count(n)
        result = 1
        c = MAX_COUNT
        for d in reversed(xrange(9+1)):
            if c == 0:
                break
            while cnt[d] and c:
                cnt[d] -= 1
                c -= 1
                result *= d
        return result