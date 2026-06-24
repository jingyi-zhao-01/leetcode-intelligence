# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-kth-bit-in-nth-binary-string
# source_path: LeetCode-Solutions-master/Python/find-kth-bit-in-nth-binary-string.py
# solution_class: Solution
# submission_id: 022056560880e79937a8a37e5c6bfc2300b9d69e
# seed: 1512458810

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        flip, l = 0, 2**n-1
        while k > 1:
            if k == l//2+1:
                flip ^= 1
                break
            if k > l//2:
                k = l+1-k
                flip ^= 1
            l //= 2
        return str(flip)