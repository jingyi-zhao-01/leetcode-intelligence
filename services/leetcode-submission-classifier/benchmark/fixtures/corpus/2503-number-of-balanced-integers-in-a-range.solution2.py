# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-balanced-integers-in-a-range
# source_path: LeetCode-Solutions-master/Python/number-of-balanced-integers-in-a-range.py
# solution_class: Solution2
# submission_id: 0afbcc8e4f04ca6df9cdeebef41907f802ac79e8
# seed: 1939610585

# Time:  O((logn)^2)
# Space: O(logn)

# dp

class Solution2(object):
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
            memo = [[-1]*(len(digits)*9+1) for _ in xrange(len(digits))]
            def memoization(i, curr, tight):
                if i == len(digits):
                    return curr == 0
                if not tight and memo[i][curr] != -1:
                    return memo[i][curr]
                bound = digits[i] if tight else 9
                result = 0
                for d in xrange(bound+1):
                    result += memoization(i+1, curr-d if i&1 else curr+d, tight and d == bound)
                if not tight:
                    memo[i][curr] = result
                return result
            
            return memoization(0, 0, True)
        
        return count(high)-count(low-1)