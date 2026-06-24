# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 3sum-closest
# source_path: LeetCode-Solutions-master/Python/3sum-closest.py
# solution_class: Solution
# submission_id: 3fc5e5ad848781aaef96ab6ac0ceb567d80922a7
# seed: 1450604361

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result, min_diff = 0, float("inf")
        nums.sort()
        for i in reversed(xrange(2, len(nums))):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            left, right = 0, i-1
            while left < right:
                total = nums[left]+nums[right]+nums[i]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
                if abs(total-target) < min_diff:
                    min_diff = abs(total-target)
                    result = total
        return result