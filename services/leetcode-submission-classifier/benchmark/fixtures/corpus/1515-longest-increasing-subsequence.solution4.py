# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-increasing-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-increasing-subsequence.py
# solution_class: Solution4
# submission_id: a787740a97e3a2d4e7cb075e26d578f04e7360a8
# seed: 4128262510

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution4(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val_to_idx = {num:i for i, num in enumerate(sorted(set(nums)))}
        st = SegmentTree(len(val_to_idx))
        for x in nums:
            st.update(val_to_idx[x], val_to_idx[x], st.query(0, val_to_idx[x]-1)+1 if val_to_idx[x] >= 1 else 1)
        return st.query(0, len(val_to_idx)-1) if len(val_to_idx) >= 1 else 0