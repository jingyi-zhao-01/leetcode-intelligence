# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-submatrices-with-all-ones
# source_path: LeetCode-Solutions-master/Python/count-submatrices-with-all-ones.py
# solution_class: Solution
# submission_id: af45524b6d33ee42a3c771f9df31838979ea1771
# seed: 2341817559

# Time:  O(m * n)
# Space: O(n)

# mono stack

class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        def count(heights):
            result = curr = 0
            stk = []
            for i in xrange(len(heights)):
                while stk and heights[stk[-1]] >= heights[i]:
                    j = stk.pop()
                    curr -= (heights[j]-heights[i])*(j-(stk[-1] if stk else -1))
                stk.append(i)
                curr += heights[i]
                result += curr
            return result

        result = 0
        heights = [0]*len(mat[0])
        for i in xrange(len(mat)):
            for j in xrange(len(mat[0])):
                heights[j] = heights[j]+1 if mat[i][j] == 1 else 0
            result += count(heights)
        return result