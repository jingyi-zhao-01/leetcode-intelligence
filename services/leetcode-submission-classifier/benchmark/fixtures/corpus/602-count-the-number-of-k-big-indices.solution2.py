# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-k-big-indices
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-k-big-indices.py
# solution_class: Solution2
# submission_id: 13dabb430a11d7b505057d1e32cbcd4ec863ea45
# seed: 3127199458

# Time:  O(nlogk)
# Space: O(n)

import heapq


# heap

class Solution2(object):
    def kBigIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sl1, sl2 = SortedList(), SortedList(nums)
        result = 0
        for x in nums:
            sl2.remove(x)
            if sl1.bisect_left(x) >= k and sl2.bisect_left(x) >= k:
                result += 1
            sl1.add(x)
        return result