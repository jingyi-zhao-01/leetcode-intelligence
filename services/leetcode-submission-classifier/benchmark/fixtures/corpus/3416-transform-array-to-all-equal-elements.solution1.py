# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: transform-array-to-all-equal-elements
# source_path: LeetCode-Solutions-master/Python/transform-array-to-all-equal-elements.py
# solution_class: Solution
# submission_id: bd7ca7eb0025ecf5bec26f686449674b4317c143
# seed: 3099082161

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def canMakeEqual(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def check(target):
            cnt = 0
            sign = 1
            for i in xrange(len(nums)):
                if nums[i]*sign == target:
                    sign = 1
                    continue
                cnt += 1
                if i+1 == len(nums) or cnt > k:
                    return False
                sign = -1
            return True

        return check(1) or check(-1)