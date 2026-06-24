# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-subarray-to-maximize-array-value
# source_path: LeetCode-Solutions-master/Python/reverse-subarray-to-maximize-array-value.py
# solution_class: Solution
# submission_id: 5da3763cd45d1f41fb250b61e703a8aa87e43058
# seed: 871383608

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, add, max_pair, min_pair = 0, 0, float("-inf"), float("inf")
        for i in xrange(1, len(nums)):
            result += abs(nums[i-1]-nums[i])
            add = max(add,
                      abs(nums[0]-nums[i]) - abs(nums[i-1]-nums[i]),
                      abs(nums[-1]-nums[i-1]) - abs(nums[i-1]-nums[i]))
            min_pair = min(min_pair, max(nums[i-1], nums[i]))
            max_pair = max(max_pair, min(nums[i-1], nums[i]))
        return result + max(add, (max_pair-min_pair)*2)