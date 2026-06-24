# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-good-partitions
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-good-partitions.py
# solution_class: Solution
# submission_id: 3efd97eccfc57b1543b4d1903c0afbdbfbebea55
# seed: 1387248536

# Time:  O(n)
# Space: O(n)

# hash table, combinatorics

class Solution(object):
    def numberOfGoodPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        lookup = {x:i for i, x in enumerate(nums)}
        result = 1
        right = cnt = 0
        for left, x in enumerate(nums):
            if left == right+1:
                cnt += 1
            right = max(right, lookup[x])
        return pow(2, cnt, MOD)