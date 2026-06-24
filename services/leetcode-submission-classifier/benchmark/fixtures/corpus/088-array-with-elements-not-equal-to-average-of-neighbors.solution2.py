# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: array-with-elements-not-equal-to-average-of-neighbors
# source_path: LeetCode-Solutions-master/Python/array-with-elements-not-equal-to-average-of-neighbors.py
# solution_class: Solution2
# submission_id: 5068df32302a66ed0d5810bdbcaac13bf9e320e9
# seed: 500314870

# Time:  O(n) ~ O(n^2), O(n) on average
# Space: O(1)

# Tri Partition (aka Dutch National Flag Problem) with virtual index solution

class Solution2(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        mid = (len(nums)-1)//2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        return nums