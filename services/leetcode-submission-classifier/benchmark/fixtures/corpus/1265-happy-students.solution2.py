# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: happy-students
# source_path: LeetCode-Solutions-master/Python/happy-students.py
# solution_class: Solution2
# submission_id: c1ef865371b0d9ae2f5a8359024d9a24d68ce537
# seed: 479574922

# Time:  O(n)
# Space: O(n)

# codeforce, https://codeforces.com/contest/1782/problem/B
# freq table

class Solution2(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum((i == 0 or nums[i-1] < i) and (i == len(nums) or nums[i] > i) for i in xrange(len(nums)+1))