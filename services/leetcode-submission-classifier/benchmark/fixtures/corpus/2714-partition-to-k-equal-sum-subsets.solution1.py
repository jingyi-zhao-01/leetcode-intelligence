# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-to-k-equal-sum-subsets
# source_path: LeetCode-Solutions-master/Python/partition-to-k-equal-sum-subsets.py
# solution_class: Solution
# submission_id: 23e80352a46866e5ca448875be020f0a0a69712a
# seed: 2584594642

# Time:  O(n*2^n)
# Space: O(2^n)

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums, target, used, todo, lookup):
            if lookup[used] is None:
                targ = (todo-1)%target + 1
                lookup[used] = any(dfs(nums, target, used | (1<<i), todo-num, lookup) \
                                   for i, num in enumerate(nums) \
                                   if ((used>>i) & 1) == 0 and num <= targ)
            return lookup[used]

        total = sum(nums)
        if total%k or max(nums) > total//k:
            return False
        lookup = [None] * (1 << len(nums))
        lookup[-1] = True
        return dfs(nums, total//k, 0, total, lookup)