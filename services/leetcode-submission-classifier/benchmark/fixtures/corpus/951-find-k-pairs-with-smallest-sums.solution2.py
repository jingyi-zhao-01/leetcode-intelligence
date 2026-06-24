# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-k-pairs-with-smallest-sums
# source_path: LeetCode-Solutions-master/Python/find-k-pairs-with-smallest-sums.py
# solution_class: Solution2
# submission_id: db3529e76ad1d915bd0a42f7c461297f5f29bc37
# seed: 1613312608

# Time:  O(k * log(min(n, m, k))), where n is the size of num1, and m is the size of num2.
# Space: O(min(n, m, k))

from heapq import heappush, heappop

class Solution2(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        return nsmallest(k, product(nums1, nums2), key=sum)