# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-distinct-subarrays-with-at-most-k-odd-integers
# source_path: LeetCode-Solutions-master/Python/number-of-distinct-subarrays-with-at-most-k-odd-integers.py
# solution_class: Solution
# submission_id: f877ba5788c450ea8d189bcd74cd0886e730dbd7
# seed: 1615541807

# Time:  O(n^2)
# Space: O(t), t is the size of trie

import collections


# sliding window + trie solution

class Solution(object):
    def distinctSubarraysWithAtMostKOddIntegers(self, A, K):
        def countDistinct(A, left, right, trie):  # Time: O(n), Space: O(t)
            result = 0
            for i in reversed(xrange(left, right+1)):
                if A[i] not in trie:
                    result += 1
                trie = trie[A[i]]
            return result

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        result, left, count = 0, 0, 0
        for right in xrange(len(A)):
            count += A[right]%2
            while count > K:
                count -= A[left]%2
                left += 1
            result += countDistinct(A, left, right, trie)
        return result