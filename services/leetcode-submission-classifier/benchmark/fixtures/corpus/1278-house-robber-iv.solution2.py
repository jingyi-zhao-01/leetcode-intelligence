# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: house-robber-iv
# source_path: LeetCode-Solutions-master/Python/house-robber-iv.py
# solution_class: Solution2
# submission_id: 2256d48e604ad565bbd30ad37ed6f074a6457660
# seed: 2617209095

# Time:  O(nlogn)
# Space: O(n)

# binary search, greedy

class Solution2(object):
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
    
        left, right = min(nums), max(nums)
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left