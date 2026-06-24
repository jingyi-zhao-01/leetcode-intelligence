# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: happy-students
# source_path: LeetCode-Solutions-master/Python/happy-students.py
# solution_class: Solution
# submission_id: 454c4664c67dbd36a355664744ffed08f2bd6895
# seed: 1233963660

# Time:  O(n)
# Space: O(n)

# codeforce, https://codeforces.com/contest/1782/problem/B
# freq table

class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = [0]*(len(nums)+1)
        for x in nums:
            cnt[x] += 1
        result = prefix = 0
        for i in xrange(len(nums)+1):
            if prefix == i and cnt[i] == 0:
                result += 1
            prefix += cnt[i]
        return result