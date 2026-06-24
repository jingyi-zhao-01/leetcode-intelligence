# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-distinct-averages
# source_path: LeetCode-Solutions-master/Python/number-of-distinct-averages.py
# solution_class: Solution
# submission_id: 33e6fadc47e2c15e4b1e202cc22e12ba368608a2
# seed: 4267020310

# Time:  O(nlogn)
# Space: O(n)

# sort, two pointers, hash table

class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = set()
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            lookup.add(nums[left]+nums[right])
            left, right = left+1, right-1
        return len(lookup)