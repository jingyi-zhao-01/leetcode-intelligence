# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-a-peak-element-ii
# source_path: LeetCode-Solutions-master/Python/find-a-peak-element-ii.py
# solution_class: Solution
# submission_id: 9b1ad468ae2c814e0b6de60cd5d1c65707307abb
# seed: 993630556

# Time:  O(min(n, m) * log(max(n, m)))
# Space: O(1)

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        def get_vec(mat, i):
            return mat[i] if len(mat) > len(mat[0]) else (mat[j][i] for j in xrange(len(mat)))

        def check(mat, x):
            return max(get_vec(mat, x)) > max(get_vec(mat, x+1))

        left, right = 0, (max(len(mat), len(mat[0]))-1)-1
        while left <= right:
            mid = left + (right-left)//2
            if check(mat, mid):
                right = mid-1
            else:
                left = mid+1
        mav_val = max(get_vec(mat, left))
        result = [left, next(i for i, x in enumerate(get_vec(mat, left)) if x == mav_val)]
        return result if len(mat) > len(mat[0]) else result[::-1]