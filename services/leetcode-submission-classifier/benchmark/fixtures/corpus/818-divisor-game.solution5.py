# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divisor-game
# source_path: LeetCode-Solutions-master/Python/divisor-game.py
# solution_class: Solution5
# submission_id: 3f39318088865bb0d1b35e0171e26149e1fcfd71
# seed: 1467882803

# Time:  O(1)
# Space: O(1)

# math

class Solution5(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def factors(n):
            for i in xrange(1, n+1):
                if n%i:
                    continue
                yield i
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in factors(n) if i != n)
            return lookup[n]

        lookup = [None]*(n+1)
        return memoization(n)