# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-chunks-to-make-sorted
# source_path: LeetCode-Solutions-master/Python/max-chunks-to-make-sorted.py
# solution_class: Solution
# submission_id: 7714a80fa6c3c6449f698dc9e318119ccd7c0e89
# seed: 2027552592

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result, max_i = 0, 0
        for i, v in enumerate(arr):
            max_i = max(max_i, v)
            if max_i == i:
                result += 1
        return result