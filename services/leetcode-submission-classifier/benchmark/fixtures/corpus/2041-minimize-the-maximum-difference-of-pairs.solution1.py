# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-maximum-difference-of-pairs
# source_path: LeetCode-Solutions-master/Python/minimize-the-maximum-difference-of-pairs.py
# solution_class: Solution
# submission_id: a0e5056e7ecc4fa5d52f0c49538749c3aacd9992
# seed: 3135362032

# Time:  O(nlogn + nlogr), r = max(nums)-min(nums)
# Space: O(1)

# sort, binary search, greedy

class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        def check(x):
            i = cnt = 0
            while i+1 < len(nums) and cnt < p:
                if nums[i+1]-nums[i] <= x:
                    i += 1
                    cnt += 1
                i += 1
            return cnt == p

        nums.sort()
        left, right = 0, nums[-1]-nums[0]
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left