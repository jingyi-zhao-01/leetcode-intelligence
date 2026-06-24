# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-erasure-value
# source_path: LeetCode-Solutions-master/Python/maximum-erasure-value.py
# solution_class: Solution
# submission_id: 0812e28c47ab6e3382c6ac349030c6e8eab70ceb
# seed: 800264693

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        prefix = [0]*(len(nums)+1)
        result, left = 0, 0
        for right, num in enumerate(nums):
            prefix[right+1] = prefix[right]+num
            if num in lookup:
                left = max(left, lookup[num]+1)
            lookup[num] = right
            result = max(result, prefix[right+1]-prefix[left])
        return result