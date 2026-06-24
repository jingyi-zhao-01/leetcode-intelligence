# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: house-robber-iv
# source_path: LeetCode-Solutions-master/Python/house-robber-iv.py
# solution_class: Solution
# submission_id: 902c88dfde94bda852089ada8c72a380fd3af9ee
# seed: 1887875624

# Time:  O(nlogn)
# Space: O(n)

# binary search, greedy

class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def check(x):
            cnt = i = 0
            while i < len(nums):
                if nums[i] <= x:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k

        sorted_nums = sorted(set(nums))
        left, right = 0, len(sorted_nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if check(sorted_nums[mid]):
                right = mid-1
            else:
                left = mid+1
        return sorted_nums[left]