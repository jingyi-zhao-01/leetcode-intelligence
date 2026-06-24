# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-integers-on-a-grid-path
# source_path: LeetCode-Solutions-master/Python/count-good-integers-on-a-grid-path.py
# solution_class: Solution
# submission_id: 799b2636c554aa59a0721040f7e355d727245e54
# seed: 988159256

# Time:  O(16 * 2 * 10 * 10)
# Space: O(16 + 2 * 10)

# dp

class Solution(object):
    def countGoodIntegersOnPath(self, l, r, directions):
        """
        :type l: int
        :type r: int
        :type directions: str
        :rtype: int
        """
        L = 16
        def count(n):
            digits = [0]*L
            for i in reversed(xrange(len(digits))):
                digits[i] = n%10
                n //= 10
            dp = [[0]*10 for _ in xrange(2)]
            dp[1][0] = 1
            for i in xrange(L):
                new_dp = [[0]*10 for _ in xrange(2)]
                for t in xrange(2):
                    bound = digits[i] if t else 9
                    for k in xrange(10):
                        if not dp[t][k]:
                            continue
                        for d in xrange(bound+1):
                            nk = k
                            if lookup[i]:
                                if d < k:
                                    continue
                                nk = d                                
                            new_dp[t and d == bound][nk] += dp[t][k]
                dp = new_dp
            return sum(sum(row) for row in dp)

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