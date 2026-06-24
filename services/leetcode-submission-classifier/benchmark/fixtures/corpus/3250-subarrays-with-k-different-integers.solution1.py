# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarrays-with-k-different-integers
# source_path: LeetCode-Solutions-master/Python/subarrays-with-k-different-integers.py
# solution_class: Solution
# submission_id: 2909ea8ba65d9ccc696286a7ea799c401f5b75ad
# seed: 3733672659

# Time:  O(n)
# Space: O(k)

import collections

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def atMostK(A, K):
            count = collections.defaultdict(int)
            result, left = 0, 0
            for right in xrange(len(A)):
                count[A[right]] += 1
                while len(count) > K:
                    count[A[left]] -= 1
                    if count[A[left]] == 0:
                        count.pop(A[left])
                    left += 1
                result += right-left+1
            return result
        
        return atMostK(A, K) - atMostK(A, K-1)