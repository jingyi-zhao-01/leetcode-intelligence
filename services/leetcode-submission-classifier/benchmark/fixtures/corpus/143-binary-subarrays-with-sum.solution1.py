# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-subarrays-with-sum
# source_path: LeetCode-Solutions-master/Python/binary-subarrays-with-sum.py
# solution_class: Solution
# submission_id: 2427f9a28ce561f89826d3d78e34965fef4dc36e
# seed: 1799337168

# Time:  O(n)
# Space: O(1)

# Two pointers solution

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        result = 0
        left, right, sum_left, sum_right = 0, 0, 0, 0
        for i, a in enumerate(A):
            sum_left += a
            while left < i and sum_left > S:
                sum_left -= A[left]
                left += 1
            sum_right += a
            while right < i and \
                  (sum_right > S or (sum_right == S and not A[right])):
                sum_right -= A[right]
                right += 1
            if sum_left == S:
                result += right-left+1
        return result