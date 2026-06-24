# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-out-of-three
# source_path: LeetCode-Solutions-master/Python/two-out-of-three.py
# solution_class: Solution
# submission_id: 3a18563392a7058a69c5d654dac8c2bd027bc688
# seed: 1135354191

# Time:  O(n)
# Space: O(min(n, r)), r is the range size of nums

import collections

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        K = 2
        cnt = collections.Counter()
        for nums in nums1, nums2, nums3:
            cnt.update(set(nums))
        return [x for x, c in cnt.iteritems() if c >= K]