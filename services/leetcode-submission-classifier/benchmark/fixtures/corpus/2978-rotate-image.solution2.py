# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-image
# source_path: LeetCode-Solutions-master/Python/rotate-image.py
# solution_class: Solution2
# submission_id: e846f5eef7c524f5b99afdd58a748211148153fd
# seed: 2095156453

# Time:  O(n^2)
# Space: O(1)

class Solution2(object):
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]