# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-size-subarray-sum
# source_path: LeetCode-Solutions-master/Python/minimum-size-subarray-sum.py
# solution_class: Solution
# submission_id: dcbabeec6f901edff2e17687c89aafe02df67c8c
# seed: 3182958104

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start = 0
        sum = 0
        min_size = float("inf")
        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start += 1

        return min_size if min_size != float("inf") else 0