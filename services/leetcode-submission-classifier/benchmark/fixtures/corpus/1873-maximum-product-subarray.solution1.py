# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-product-subarray.py
# solution_class: Solution
# submission_id: 32dea73164d5aef50b023542c101120af4739774
# seed: 3059069752

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:
            local_max, local_min = max(x, local_max * x, local_min * x), min(x, local_max * x, local_min * x)
            global_max = max(global_max, local_max)
        return global_max