# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-after-binary-swaps
# source_path: LeetCode-Solutions-master/Python/maximum-score-after-binary-swaps.py
# solution_class: Solution
# submission_id: d60f6eb042c8f7dbd1e5b919c86016c74aea1c66
# seed: 2936178433

# Time:  O(nlogn)
# Space: O(n)

# heap

class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        result = 0
        max_heap = []
        for i in xrange(len(nums)):
            heapq.heappush(max_heap, -nums[i])
            if s[i] == '1':
                result += -heapq.heappop(max_heap)
        return result