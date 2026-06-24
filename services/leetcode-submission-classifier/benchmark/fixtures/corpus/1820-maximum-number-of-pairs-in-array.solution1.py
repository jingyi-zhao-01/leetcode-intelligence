# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-pairs-in-array
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-pairs-in-array.py
# solution_class: Solution
# submission_id: f1ee273f1e64f14b850b2d29a22524c6ab410a68
# seed: 3534013666

# Time:  O(n)
# Space: O(r), r = max(nums)

# freq table

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = [0]*(max(nums)+1)
        pair_cnt = 0
        for x in nums:
            cnt[x] ^= 1
            if not cnt[x]:
                pair_cnt += 1
        return [pair_cnt, len(nums)-2*pair_cnt]