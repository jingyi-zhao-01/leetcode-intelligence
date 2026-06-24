# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-sum-less-than-k
# source_path: LeetCode-Solutions-master/Python/two-sum-less-than-k.py
# solution_class: Solution
# submission_id: 788b671ddcb03744c12357ae08f33cf27990ab26
# seed: 473702164

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        result = -1
        left, right = 0, len(A)-1
        while left < right:
            if A[left]+A[right] >= K:
                right -= 1
            else:
                result = max(result, A[left]+A[right])
                left += 1
        return result