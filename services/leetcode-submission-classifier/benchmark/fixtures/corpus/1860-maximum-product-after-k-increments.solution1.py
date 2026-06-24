# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-after-k-increments
# source_path: LeetCode-Solutions-master/Python/maximum-product-after-k-increments.py
# solution_class: Solution
# submission_id: 85b8471f3344a9efd2d243941728e0a152eb3649
# seed: 3228898257

# Time:  O(nlogn)
# Space: O(1)

# math, sort

class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        nums.sort()
        total = sum(nums)
        for i in reversed(xrange(len(nums))):
            if nums[i]*(i+1)-total <= k:
                break
            total -= nums[i]
        q, r = divmod(k+total, i+1)
        return (pow(q, (i+1)-r, MOD)*pow(q+1, r, MOD)*
                reduce(lambda x, y: x*y%MOD, (nums[j] for j in xrange(i+1, len(nums))), 1)) % MOD