# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: set-mismatch
# source_path: LeetCode-Solutions-master/Python/set-mismatch.py
# solution_class: Solution3
# submission_id: 964c694161358e53382e3339187a08fe2808870c
# seed: 2442179549

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        x_minus_y = sum(nums) - N*(N+1)//2
        x_plus_y = (sum(x*x for x in nums) - N*(N+1)*(2*N+1)/6) // x_minus_y
        return (x_plus_y+x_minus_y) // 2, (x_plus_y-x_minus_y) // 2