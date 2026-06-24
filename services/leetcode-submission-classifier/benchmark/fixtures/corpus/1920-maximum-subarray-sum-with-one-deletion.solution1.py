# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subarray-sum-with-one-deletion
# source_path: LeetCode-Solutions-master/Python/maximum-subarray-sum-with-one-deletion.py
# solution_class: Solution
# submission_id: baa5620289db32bc40212ebe956309b19470dcb2
# seed: 1211033076

class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result, prev, curr = float("-inf"), float("-inf"), float("-inf")
        for x in arr:
            curr = max(prev, curr+x, x)
            result = max(result, curr)
            prev = max(prev+x, x)
        return result