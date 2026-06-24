# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-and-merge-array-transformation
# source_path: LeetCode-Solutions-master/Python/split-and-merge-array-transformation.py
# solution_class: Solution2
# submission_id: ab48e7cd49a041b497949f60196cc03fbde06400
# seed: 1756234219

# Time:  O(n^4 * n!)
# Space: O(n * n!)

# bfs

class Solution2(object):
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
            lookup = {start}
            q = [start]
            while q:
                new_q = []
                for u in q:
                    if u == target:
                        return d
                    for v in adj(u):
                        if v in lookup:
                            continue
                        lookup.add(v)
                        new_q.append(v)
                q = new_q
                d += 1
            return -1

        return bfs(tuple(nums1), tuple(nums2))