# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-equal-numbers-blocks
# source_path: LeetCode-Solutions-master/Python/number-of-equal-numbers-blocks.py
# solution_class: Solution
# submission_id: 95dcfd60f1fc8fe90b19530a63816a19b5737772
# seed: 750981191

# Time:  O(klogn), k = len(set(nums))
# Space: O(1)

# Definition for BigArray.
class BigArray:
    def at(self, index):
        pass
    def size(self):
        pass


# binary search

class Solution(object):
    def countBlocks(self, nums):
        """
        :type nums: BigArray
        :rtype: int
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        n = nums.size()
        result = left = 0
        while left != n:
            target = nums.at(left)
            left = binary_search_right(left, n-1, lambda x: nums.at(x) == target)+1
            result += 1
        return result