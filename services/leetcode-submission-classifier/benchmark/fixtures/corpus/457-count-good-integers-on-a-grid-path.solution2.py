# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-integers-on-a-grid-path
# source_path: LeetCode-Solutions-master/Python/count-good-integers-on-a-grid-path.py
# solution_class: Solution2
# submission_id: c0a354a5cc0c687d73892882b30ee8db070ad729
# seed: 1008923620

# Time:  O(16 * 2 * 10 * 10)
# Space: O(16 + 2 * 10)

# dp

class Solution2(object):
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
                if not t and memo[i][k] != -1:
                    return memo[i][k]
                result = 0
                bound = digits[i] if t else 9
                for d in xrange(bound+1):
                    nk = k
                    if lookup[i]:
                        if d < k:
                            continue
                        nk = d   
                    result += memoization(i+1, t and d == bound, nk)
                if not t:
                    memo[i][k] = result
                return result

            digits = [0]*L
            for i in reversed(xrange(len(digits))):
                digits[i] = n%10
                n //= 10
            memo = [[-1]*10 for _ in xrange(L)]
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