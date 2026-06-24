# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-maximum-of-array
# source_path: LeetCode-Solutions-master/Python/minimize-maximum-of-array.py
# solution_class: Solution
# submission_id: 755c2f8d7fd92e7693166adde6307971d0f95a0b
# seed: 1479352050

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        result = curr = 0
        for i, x in enumerate(nums):
            curr += x
            result = max(result, ceil_divide(curr, i+1))
        return result