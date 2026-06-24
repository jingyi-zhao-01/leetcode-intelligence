# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divisor-game
# source_path: LeetCode-Solutions-master/Python/divisor-game.py
# solution_class: Solution3
# submission_id: c2611ffe2d6bf971a6ff08de7837d71c53d8a7bf
# seed: 90585434

# Time:  O(1)
# Space: O(1)

# math

class Solution3(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def factors(n):
            result = [[] for _ in xrange(n+1)]
            for i in xrange(1, n+1):
                for j in range(i, n+1, i):
                    result[j].append(i)
            return result
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in FACTORS[n] if i != n)
            return lookup[n]

        FACTORS = factors(n)
        lookup = [None]*(n+1)
        return memoization(n)