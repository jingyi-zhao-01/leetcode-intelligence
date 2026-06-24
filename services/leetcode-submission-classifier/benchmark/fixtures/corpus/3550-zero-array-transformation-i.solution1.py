# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zero-array-transformation-i
# source_path: LeetCode-Solutions-master/Python/zero-array-transformation-i.py
# solution_class: Solution
# submission_id: 63e0fa73643ee6557681f00c634d4994843dcf27
# seed: 981279145

# Time:  O(n + q)
# Space: O(n)

# line sweep

class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        events = [0]*(len(nums)+1)
        for l, r in queries:
            events[l] += 1
            events[r+1] -= 1
        curr = 0
        for i in xrange(len(nums)):
            curr += events[i]
            if nums[i] > curr:
                return False
        return True