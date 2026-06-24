# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-achievable-transfer-requests
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-achievable-transfer-requests.py
# solution_class: Solution
# submission_id: 3d6b5035c727582fb2c9b0e53c686eb9e4a71fb0
# seed: 4208389945

# Time:  O((n + r) * 2^r)
# Space: O(n + r)

import itertools


# early return solution

class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        for k in reversed(xrange(1, len(requests)+1)):
            for c in itertools.combinations(xrange(len(requests)), k):
                change = [0]*n
                for i in c:
                    change[requests[i][0]] -= 1
                    change[requests[i][1]] += 1
                if all(c == 0 for c in change):
                    return k  # early return
        return 0