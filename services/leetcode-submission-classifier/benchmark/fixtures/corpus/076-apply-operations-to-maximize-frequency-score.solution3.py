# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-maximize-frequency-score
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-maximize-frequency-score.py
# solution_class: Solution3
# submission_id: 2d4012da4f8dedcde7e266f5acb37e4f0150aef3
# seed: 3501552159

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers, sliding window

class Solution3(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def check(l):
            # "-+ " or "-0+"
            return any((prefix[i+l]-prefix[i+(l+1)//2])-(prefix[i+l//2]-prefix[i]) <= k for i in xrange(len(nums)-l+1))

        nums.sort()
        prefix = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i]+x
        left, right = 1, len(nums)
        while left <= right:
            mid = left+(right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right