# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-partitions-with-even-sum-difference
# source_path: LeetCode-Solutions-master/Python/count-partitions-with-even-sum-difference.py
# solution_class: Solution
# submission_id: 1e69f9a07399314becee4badcddae4e0105c3087
# seed: 1230505649

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = left = 0
        right = sum(nums)
        for i in xrange(len(nums)-1):
            left += nums[i]
            right -= nums[i]
            if left%2 == right%2:
                result += 1
        return result