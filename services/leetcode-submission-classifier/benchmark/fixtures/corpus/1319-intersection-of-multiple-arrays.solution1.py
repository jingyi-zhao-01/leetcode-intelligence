# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-multiple-arrays
# source_path: LeetCode-Solutions-master/Python/intersection-of-multiple-arrays.py
# solution_class: Solution
# submission_id: b728956f74f574864cd70bec7dd9b82e4ad15556
# seed: 712831215

# Time:  O(n * l + r), n = len(nums), l = len(nums[0])
# Space: O(r), r = max(nums)-min(nums)

# freq table, counting sort

class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        MAX_NUM = 1000
        cnt = [0]*(MAX_NUM+1)
        for num in nums:
            for x in num:
                cnt[x] += 1
        return [i for i in xrange(1, MAX_NUM+1) if cnt[i] == len(nums)]