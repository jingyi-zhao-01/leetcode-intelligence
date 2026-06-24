# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-achievable-transfer-requests
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-achievable-transfer-requests.py
# solution_class: Solution2
# submission_id: 8c5383a8d9c98c1c92f5438b86b3babab058b165
# seed: 1367741542

# Time:  O((n + r) * 2^r)
# Space: O(n + r)

import itertools


# early return solution

class Solution2(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        def evaluate(n, requests, mask):
            change = [0]*n
            base, count = 1, 0
            for i in xrange(len(requests)):
                if base & mask:
                    change[requests[i][0]] -= 1
                    change[requests[i][1]] += 1
                    count += 1
                base <<= 1
            return count if all(c == 0 for c in change) else 0

        return max(evaluate(n, requests, i) for i in xrange(1 << len(requests)))