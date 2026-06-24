# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-to-k-equal-sum-subsets
# source_path: LeetCode-Solutions-master/Python/partition-to-k-equal-sum-subsets.py
# solution_class: Solution2
# submission_id: 620a7e12e41823cfa03c07fcca161833bee5f10d
# seed: 2769259584

# Time:  O(n*2^n)
# Space: O(2^n)

class Solution2(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums, target, i, subset_sums):
            if i == len(nums):
                return True
            for k in xrange(len(subset_sums)):
                if subset_sums[k]+nums[i] > target:
                    continue
                subset_sums[k] += nums[i]
                if dfs(nums, target, i+1, subset_sums):
                    return True
                subset_sums[k] -= nums[i]
                if not subset_sums[k]: break
            return False

        total = sum(nums)
        if total%k != 0 or max(nums) > total//k:
            return False
        nums.sort(reverse=True)
        subset_sums = [0] * k
        return dfs(nums, total//k, 0, subset_sums)