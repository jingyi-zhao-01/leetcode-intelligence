# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-array-largest-sum
# source_path: LeetCode-Solutions-master/Python/split-array-largest-sum.py
# solution_class: Solution
# submission_id: 5e9ffa6084e60af5a49378378a53c588c1d2703b
# seed: 2906406976

# Time:  O(nlogs), s is the sum of nums
# Space: O(1)

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def check(nums, m, s):
            cnt, curr_sum = 1, 0
            for num in nums:
                curr_sum += num
                if curr_sum > s:
                    curr_sum = num
                    cnt += 1
            return cnt <= m

        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if check(nums, m, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left