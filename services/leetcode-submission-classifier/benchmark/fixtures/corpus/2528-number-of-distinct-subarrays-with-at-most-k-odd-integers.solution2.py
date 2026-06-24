# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-distinct-subarrays-with-at-most-k-odd-integers
# source_path: LeetCode-Solutions-master/Python/number-of-distinct-subarrays-with-at-most-k-odd-integers.py
# solution_class: Solution2
# submission_id: a102f4974691fa12c53f307f154de7f7b6d95a22
# seed: 1575283142

# Time:  O(n^2)
# Space: O(t), t is the size of trie

import collections


# sliding window + trie solution

class Solution2(object):
    def distinctSubarraysWithAtMostKOddIntegers(self, A, K):
        def countDistinct(A, left, right, trie):  # Time: O(n), Space: O(t)
            result = 0
            for i in xrange(left, right+1):
                if A[i] not in trie:
                    result += 1
                trie = trie[A[i]]
            return result

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        result = 0
        for left in xrange(len(A)):
            count = 0
            for right in xrange(left, len(A)):
                count += A[right]%2
                if count > K:
                    right -= 1
                    break
            result += countDistinct(A, left, right, trie)
        return result