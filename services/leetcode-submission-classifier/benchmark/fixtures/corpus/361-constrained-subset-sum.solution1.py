# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: constrained-subset-sum
# source_path: LeetCode-Solutions-master/Python/constrained-subset-sum.py
# solution_class: Solution
# submission_id: 996aa8b6df61f0fb8822833db21997e8aa461870
# seed: 3222466103

# Time:  O(n)
# Space: O(k)

import collections

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result, dq = float("-inf"), collections.deque()
        for i in xrange(len(nums)):
            if dq and i-dq[0][0] == k+1:
                dq.popleft()
            curr = nums[i] + (dq[0][1] if dq else 0)
            while dq and dq[-1][1] <= curr:
                dq.pop()
            if curr > 0:
                dq.append((i, curr))
            result = max(result, curr)
        return result