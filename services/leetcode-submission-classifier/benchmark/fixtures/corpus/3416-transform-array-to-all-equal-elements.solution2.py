# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: transform-array-to-all-equal-elements
# source_path: LeetCode-Solutions-master/Python/transform-array-to-all-equal-elements.py
# solution_class: Solution2
# submission_id: 7450d7300a6d8924d4d2f560ce8af05a11ad21bc
# seed: 2187418301

# Time:  O(n)
# Space: O(1)

# greedy

class Solution2(object):
    def canMakeEqual(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def check(target):
            parity = cnt = 0
            for i in xrange(len(nums)):
                if nums[i] == target:
                    continue
                cnt += i if parity else -i
                if cnt > k:
                    return False
                parity ^= 1
            return parity == 0

        return check(1) or check(-1)