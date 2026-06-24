# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-steps-to-reduce-a-number-to-zero
# source_path: LeetCode-Solutions-master/Python/number-of-steps-to-reduce-a-number-to-zero.py
# solution_class: Solution
# submission_id: 16f3386631d8637f15d40d92489db365cb691c87
# seed: 364325262

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while num:
            result += 2 if num%2 else 1
            num //= 2
        return max(result-1, 0)