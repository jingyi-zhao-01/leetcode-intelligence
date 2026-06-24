# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divisor-game
# source_path: LeetCode-Solutions-master/Python/divisor-game.py
# solution_class: Solution4
# submission_id: c34fcd7ca6a1feb22e786ecb7cd13d11b83ba988
# seed: 3869325690

# Time:  O(1)
# Space: O(1)

# math

class Solution4(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def factors(n):
            for i in xrange(1, n+1):
                if i*i > n:
                    break
                if n%i:
                    continue
                yield i
                if n//i != i:
                    yield n//i
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in factors(n) if i != n)
            return lookup[n]

        lookup = [None]*(n+1)
        return memoization(n)