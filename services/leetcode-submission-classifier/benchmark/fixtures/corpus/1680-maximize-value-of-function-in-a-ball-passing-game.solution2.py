# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-value-of-function-in-a-ball-passing-game
# source_path: LeetCode-Solutions-master/Python/maximize-value-of-function-in-a-ball-passing-game.py
# solution_class: Solution2
# submission_id: 5d4f26f4470c2ecde1e5c3b8a46176db61c41fbc
# seed: 719036685

# Time:  O(n)
# Space: O(n)

import collections


# graph, prefix sum, two pointers, sliding window

class Solution2(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        l = (k+1).bit_length()
        P = [receiver[:] for _ in xrange(l)]
        S = [range(len(receiver)) for _ in xrange(l)]
        for i in xrange(1, len(P)):
            for u in xrange(len(receiver)):
                P[i][u] = P[i-1][P[i-1][u]]
                S[i][u] = S[i-1][u]+S[i-1][P[i-1][u]]
        result = 0
        for u in xrange(len(receiver)):
            curr = 0
            for i in xrange(l):
                if (k+1)&(1<<i):
                    curr += S[i][u]
                    u = P[i][u]
            result = max(result, curr)
        return result