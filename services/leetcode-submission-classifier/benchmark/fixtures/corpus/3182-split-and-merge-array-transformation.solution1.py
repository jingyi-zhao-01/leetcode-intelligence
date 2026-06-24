# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-and-merge-array-transformation
# source_path: LeetCode-Solutions-master/Python/split-and-merge-array-transformation.py
# solution_class: Solution
# submission_id: 818af8585c51cc4fb51b8b12ccddfcc5cddbf41c
# seed: 2140254370

# Time:  O(n^4 * n!)
# Space: O(n * n!)

# bfs

class Solution(object):
    def minSplitMerge(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def bfs(start, target):
            def adj(arr):
                for l in xrange(len(arr)):
                    for r in xrange(l, len(arr)):
                        sub = arr[l:r+1]
                        rem = arr[:l]+arr[r+1:]
                        for i in xrange(len(rem)+1):
                            if i == l:
                                continue
                            yield rem[:i]+sub+rem[i:]

            d = 0
            if start == target:
                return d
            lookup = {start}
            q = [start]
            d += 1
            while q:
                new_q = []
                for u in q:
                    for v in adj(u):
                        if v in lookup:
                            continue
                        if v == target:
                            return d
                        lookup.add(v)
                        new_q.append(v)
                q = new_q
                d += 1
            return -1
    
        return bfs(tuple(nums1), tuple(nums2))