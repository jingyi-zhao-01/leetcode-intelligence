# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flipping-an-image
# source_path: LeetCode-Solutions-master/Python/flipping-an-image.py
# solution_class: Solution
# submission_id: 1fa1ece5dcf1b3b4d44d8936338ae2bd02ba12af
# seed: 2966711488

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in xrange((len(row)+1) // 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A