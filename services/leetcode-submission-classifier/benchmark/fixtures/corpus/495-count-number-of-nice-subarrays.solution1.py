# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-nice-subarrays
# source_path: LeetCode-Solutions-master/Python/count-number-of-nice-subarrays.py
# solution_class: Solution
# submission_id: 06a448b6afa491c3ff30c6bf98b8455fa22e47df
# seed: 4256705152

# Time:  O(n)
# Space: O(k)

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(nums, k):
            result, left, count = 0, 0, 0
            for right, x in enumerate(nums):
                count += x%2
                while count > k:
                    count -= nums[left]%2
                    left += 1
                result += right-left+1
            return result

        return atMost(nums, k) - atMost(nums, k-1)