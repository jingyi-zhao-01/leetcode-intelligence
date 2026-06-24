# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-connected-groups-by-inserting-interval
# source_path: LeetCode-Solutions-master/Python/minimize-connected-groups-by-inserting-interval.py
# solution_class: Solution
# submission_id: d050b1ffe745907220f61d31afcb5f9a71d58c42
# seed: 3522710689

# Time:  O(nlogn)
# Space: O(n)

# sort, prefix sum, two pointers, sliding window

class Solution(object):
    def minConnectedGroups(self, intervals, k):
        """
        :type intervals: List[List[int]]
        :type k: int
        :rtype: int
        """
        intervals.sort()
        result = 0
        prefix = [0]*(len(intervals)+1)
        mx = float("-inf")
        left = 0
        for right in xrange(len(intervals)):
            prefix[right+1] = prefix[right]+int(mx < intervals[right][0])
            mx = max(mx, intervals[right][1])
            while intervals[right][0]-intervals[left][1] > k:
                left += 1
            result = max(result, prefix[right+1]-prefix[left+1])
        return prefix[-1]-result