# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows
# source_path: LeetCode-Solutions-master/Python/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows.py
# solution_class: Solution2
# submission_id: d981c9fdfc10b9715af3de8ffd5e50f7d21ecc97
# seed: 1570545346

# Time:  O(m * klogk)
# Space: O(k)

import heapq

class Solution2(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """        
        def countArraysHaveSumLessOrEqual(mat, k, r, target):  # Time: O(k + m) ~ O(k * m)
            if target < 0:
                return 0
            if r == len(mat):
                return 1
            result = 0
            for c in xrange(len(mat[0])):
                cnt = countArraysHaveSumLessOrEqual(mat, k-result, r+1, target-mat[r][c])
                if not cnt:
                    break
                result += cnt
                if result > k:
                    break
            return result
        
        max_num = max(x for row in mat for x in row)
        left, right = len(mat), len(mat)*max_num
        while left <= right:
            mid = left + (right-left)//2
            cnt = countArraysHaveSumLessOrEqual(mat, k, 0, mid)
            if cnt >= k:
                right = mid-1
            else:
                left = mid+1
        return left