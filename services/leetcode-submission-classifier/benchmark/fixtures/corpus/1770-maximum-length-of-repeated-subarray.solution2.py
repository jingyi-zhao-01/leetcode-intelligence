# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-repeated-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-repeated-subarray.py
# solution_class: Solution2
# submission_id: 2ab745b522eb9961cffbae23caa8b5fc5555e65b
# seed: 3728165169

# Time:  O(m * n)
# Space: O(min(m, n))

import collections

class Solution2(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) > len(B): return self.findLength(B, A)
        M, p = 10**9+7, 113
        p_inv = pow(p, M-2, M)
        def check(guess):
            def rolling_hashes(source, length):
                if length == 0:
                    yield 0, 0
                    return

                val, power = 0, 1
                for i, x in enumerate(source):
                    val = (val + x*power) % M
                    if i < length - 1:
                        power = (power*p) % M
                    else:
                        yield val, i-(length-1)
                        val = (val-source[i-(length-1)])*p_inv % M

            hashes = collections.defaultdict(list)
            for hash_val, i in rolling_hashes(A, guess):
                hashes[hash_val].append(i)
            for hash_val, j in rolling_hashes(B, guess):
                if any(A[i:i+guess] == B[j:j+guess] for i in hashes[hash_val]):
                    return True
            return False

        left, right = 0, min(len(A), len(B)) + 1
        while left < right:
            mid = left + (right-left)/2
            if not check(mid):  # find the min idx such that check(idx) == false
                right = mid
            else:
                left = mid+1
        return left-1