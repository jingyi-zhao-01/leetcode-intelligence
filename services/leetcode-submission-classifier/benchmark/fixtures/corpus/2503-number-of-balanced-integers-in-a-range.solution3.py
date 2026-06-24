# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-balanced-integers-in-a-range
# source_path: LeetCode-Solutions-master/Python/number-of-balanced-integers-in-a-range.py
# solution_class: Solution3
# submission_id: b1214de70a2e3ffc4d755046ba69430fd327316f
# seed: 3066154314

# Time:  O((logn)^2)
# Space: O(logn)

# dp

class Solution3(object):
    def countBalanced(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def count(n):
            digits = []
            while n:
                n, r = divmod(n, 10)
                digits.append(r)
            digits.reverse()
            memo = [[[-1]*2 for _ in xrange(len(digits)*9+1)] for _ in xrange(len(digits))]
            def memoization(i, curr, tight):
                if i == len(digits):
                    return int(curr == 0)
                if memo[i][curr][tight] == -1:
                    bound = digits[i] if tight else 9
                    result = 0
                    for d in xrange(bound+1):
                        result += memoization(i+1, curr-d if i&1 else curr+d, tight and d == bound)
                    memo[i][curr][tight] = result
                return memo[i][curr][tight]
            
            return memoization(0, 0, True)
        
        return count(high)-count(low-1)