# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-integers-on-a-grid-path
# source_path: LeetCode-Solutions-master/Python/count-good-integers-on-a-grid-path.py
# solution_class: Solution3
# submission_id: bcab5b5ffda60eb008fd350633e13338a0352903
# seed: 2091370441

# Time:  O(16 * 2 * 10 * 10)
# Space: O(16 + 2 * 10)

# dp

class Solution3(object):
    def countGoodIntegersOnPath(self, l, r, directions):
        """
        :type l: int
        :type r: int
        :type directions: str
        :rtype: int
        """
        L = 16
        def count(n):
            def memoization(i, t, k):
                if i == L:
                    return 1
                if memo[i][t][k] == -1:
                    memo[i][t][k] = 0
                    bound = digits[i] if t else 9
                    for d in xrange(bound+1):
                        nk = k
                        if lookup[i]:
                            if d < k:
                                continue
                            nk = d   
                        memo[i][t][k] += memoization(i+1, t and d == bound, nk)
                return memo[i][t][k]

            digits = [0]*L
            for i in reversed(xrange(len(digits))):
                digits[i] = n%10
                n //= 10
            memo = [[[-1]*10 for _ in xrange(2)] for _ in xrange(L)]
            return memoization(0, True, 0)

        i = j = 0
        lookup = [False]*L
        lookup[i*4+j] = True
        for x in directions:
            if x == 'D':
                i += 1
            else:
                j += 1
            lookup[i*4+j] = True
        return count(r)-count(l-1)