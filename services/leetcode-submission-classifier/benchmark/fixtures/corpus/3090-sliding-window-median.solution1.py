# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sliding-window-median
# source_path: LeetCode-Solutions-master/Python/sliding-window-median.py
# solution_class: Solution
# submission_id: 71c200b8302716770a4937e54be2a084fdcd5fe3
# seed: 1522059720

# Time:  O(nlogk)
# Space: O(k)

from sortedcontainers import SortedList

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        sl = SortedList(float(nums[i])for i in xrange(k))
        result = [(sl[k//2]+sl[k//2-(1-k%2)])/2]
        for i in xrange(k, len(nums)):
            sl.add(float(nums[i]))
            sl.remove(nums[i-k])
            result.append((sl[k//2]+sl[k//2-(1-k%2)])/2)
        return result