# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsequence-sum-after-capping-elements
# source_path: LeetCode-Solutions-master/Python/subsequence-sum-after-capping-elements.py
# solution_class: Solution
# submission_id: 5672737de0611566ca3549b9184ed3a640099a81
# seed: 760346574

# Time:  O(nlogn + n * k + klogn) = O(nlogn + n * k)
# Space: O(k)

# sort, dp, bitmasks

class Solution(object):
    def subsequenceSumAfterCapping(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[bool]
        """
        result = [False]*len(nums)
        nums.sort()
        mask = (1<<(k+1))-1
        dp = 1
        i = 0
        for x in xrange(1, len(nums)+1):
            while i < len(nums) and nums[i] < x:
                dp |= (dp<<nums[i])&mask
                i += 1
            for j in xrange(max(k%x, k-(len(nums)-i)*x), k+1, x):
                if dp&(1<<j):
                    result[x-1] = True
                    break
        return result