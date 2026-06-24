# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-perimeter-triangle
# source_path: LeetCode-Solutions-master/Python/largest-perimeter-triangle.py
# solution_class: Solution
# submission_id: c47f7e6e2dcace365eb5db8e9f9b3dae24569b55
# seed: 2944330641

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in reversed(xrange(len(A) - 2)):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0