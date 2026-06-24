# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-product-subarray.py
# solution_class: Solution2
# submission_id: 4f8715e169a3f017bc65957666a936c93bbc46d8
# seed: 1653915659

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:
            local_max = max(1, local_max)
            if x > 0:
                local_max, local_min = local_max * x, local_min * x
            else:
                local_max, local_min = local_min * x, local_max * x
            global_max = max(global_max, local_max)
        return global_max