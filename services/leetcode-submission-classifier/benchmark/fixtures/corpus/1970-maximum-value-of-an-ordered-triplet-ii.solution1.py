# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-value-of-an-ordered-triplet-ii
# source_path: LeetCode-Solutions-master/Python/maximum-value-of-an-ordered-triplet-ii.py
# solution_class: Solution
# submission_id: 4856ef4fd1e90f8ff8ee26a494d73d1c2c9d8e6a
# seed: 2540980177

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG_INF = float("-inf")
        result = 0
        mx_diff = mx = NEG_INF
        for x in nums:
            if mx_diff != NEG_INF:
                result = max(result, mx_diff*x)
            if mx != NEG_INF:
                mx_diff = max(mx_diff, mx-x)
            mx = max(mx, x)
        return result