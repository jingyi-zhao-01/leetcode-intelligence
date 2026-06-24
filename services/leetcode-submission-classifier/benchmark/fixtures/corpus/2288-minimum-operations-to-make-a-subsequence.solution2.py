# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-a-subsequence
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-a-subsequence.py
# solution_class: Solution2
# submission_id: 0d0bb72d60e09b1281908bd536b8cc3bf8df79f1
# seed: 495607018

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution2(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        lookup = {x:i for i, x in enumerate(target)}
        st = SegmentTree(len(lookup))
        for x in arr:
            if x not in lookup:
                continue
            st.update(lookup[x], lookup[x], st.query(0, lookup[x]-1)+1 if lookup[x] >= 1 else 1)
        return len(target)-(st.query(0, len(lookup)-1) if len(lookup) >= 1 else 0)