# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-arithmetic-sequence-after-changing-at-most-one-element
# source_path: LeetCode-Solutions-master/Python/longest-arithmetic-sequence-after-changing-at-most-one-element.py
# solution_class: Solution
# submission_id: 7533f48424883e6f693b443d29e32ca24b7de29b
# seed: 3948481536

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def longestArithmetic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(nums):
            result = 2
            diff = nums[1]-nums[0]
            left = 0
            for right in xrange(2, len(nums)):
                curr = nums[right]-nums[right-1]
                if curr == diff:
                    result = max(result, right-left+1)
                    continue
                r = right
                while r+1 < len(nums) and nums[r+1]-(nums[r] if r != right else nums[r-1]+diff) == diff:
                    r += 1
                result = max(result, r-left+1)
                left = right-1
                diff = curr
            return result

        result = f(nums)
        nums.reverse()
        result = max(result, f(nums))
        return result