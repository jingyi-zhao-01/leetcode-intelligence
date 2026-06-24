# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-duplicate-number
# source_path: LeetCode-Solutions-master/Python/find-the-duplicate-number.py
# solution_class: Solution2
# submission_id: 7b0183a7347cf82540ee84b80d8f713db84742f1
# seed: 2386900389

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2
            # Get count of num <= mid.
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left