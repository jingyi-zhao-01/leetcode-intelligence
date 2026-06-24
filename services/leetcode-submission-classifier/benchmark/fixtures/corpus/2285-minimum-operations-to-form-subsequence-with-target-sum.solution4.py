# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-form-subsequence-with-target-sum
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-form-subsequence-with-target-sum.py
# solution_class: Solution4
# submission_id: 1ff200cf8a1c73babc00948dcc881d9854d7e637
# seed: 992347434

# Time:  O(n)
# Space: O(logn)

# codeforces, https://codeforces.com/problemset/problem/1303/D
# counting sort, greedy

class Solution4(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def floor_log2_x(x):
            return x.bit_length()-1

        if sum(nums) < target:
            return -1

        cnt = [0]*(floor_log2_x(max(nums))+1)
        for x in nums:
            cnt[floor_log2_x(x)] += 1
        result = i = 0
        while i < len(cnt):
            if target&(1<<i):
                if not cnt[i]:
                    j = next(j for j in xrange(i, len(cnt)) if cnt[j])
                    result += j-i
                    j = i
                    cnt[i] -= 1
                    continue
                cnt[i] -= 1
            if i+1 < len(cnt):
                cnt[i+1] += cnt[i]//2
            i += 1
        return result