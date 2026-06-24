# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-out-of-three
# source_path: LeetCode-Solutions-master/Python/two-out-of-three.py
# solution_class: Solution2
# submission_id: 4be905a43deb7f7f86ae8a4c9722fb77c74aede0
# seed: 844358275

# Time:  O(n)
# Space: O(min(n, r)), r is the range size of nums

import collections

class Solution2(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        K = 2
        cnt = collections.Counter()
        result = []
        for nums in nums1, nums2, nums3:
            for x in set(nums):
                cnt[x] += 1
                if cnt[x] == K:
                    result.append(x)
        return result