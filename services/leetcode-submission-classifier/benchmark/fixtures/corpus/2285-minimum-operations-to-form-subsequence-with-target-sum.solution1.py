# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-form-subsequence-with-target-sum
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-form-subsequence-with-target-sum.py
# solution_class: Solution
# submission_id: 41da8b1670f469f42a10c31b4d5cbdd90e2ca032
# seed: 4094652448

# Time:  O(n)
# Space: O(logn)

# codeforces, https://codeforces.com/problemset/problem/1303/D
# counting sort, greedy

class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def floor_log2_x(x):
            return x.bit_length()-1

        total = sum(nums)
        if total < target:
            return -1

        cnt = [0]*(floor_log2_x(max(nums))+1)
        for x in nums:
            cnt[floor_log2_x(x)] += 1
        result = 0
        for i in reversed(xrange(len(cnt))):
            for _ in xrange(cnt[i]):
                x = 1<<i
                if x <= target:
                    target -= x
                    total -= x
                elif total-x >= target:
                    total -= x
                else:
                    cnt[i-1] += 2
                    result += 1
        return result