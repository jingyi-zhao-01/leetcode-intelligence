# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-increment-to-make-array-unique
# source_path: LeetCode-Solutions-master/Python/minimum-increment-to-make-array-unique.py
# solution_class: Solution
# submission_id: 95a9b114b7fed45118c62a065ddadeb69c511752
# seed: 2460641273

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        A.append(float("inf"))
        result, duplicate = 0, 0
        for i in xrange(1, len(A)):
            if A[i-1] == A[i]:
                duplicate += 1
                result -= A[i]
            else:
                move = min(duplicate, A[i]-A[i-1]-1)
                duplicate -= move
                result += move*A[i-1] + move*(move+1)//2
        return result