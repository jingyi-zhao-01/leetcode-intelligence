# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-consecutive-ones-iii
# source_path: LeetCode-Solutions-master/Python/max-consecutive-ones-iii.py
# solution_class: Solution
# submission_id: fb8fd3d340ccda7c89bcc73a856a739b1b427780
# seed: 2907010076

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result, i = 0, 0
        for j in xrange(len(A)):
            K -= int(A[j] == 0)
            while K < 0:
                K += int(A[i] == 0)
                i += 1
            result = max(result, j-i+1)
        return result