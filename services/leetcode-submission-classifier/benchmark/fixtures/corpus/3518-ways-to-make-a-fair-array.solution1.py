# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ways-to-make-a-fair-array
# source_path: LeetCode-Solutions-master/Python/ways-to-make-a-fair-array.py
# solution_class: Solution
# submission_id: bc2ae6a2dcabd60894c6bbaf9f4a99fc2a80275e
# seed: 2220351359

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]*2
        suffix = [sum(nums[i] for i in xrange(k, len(nums), 2)) for k in xrange(2)]
        result = 0
        for i, num in enumerate(nums):
            suffix[i%2] -= num
            result += int(prefix[0]+suffix[1] == prefix[1]+suffix[0])
            prefix[i%2] += num
        return result