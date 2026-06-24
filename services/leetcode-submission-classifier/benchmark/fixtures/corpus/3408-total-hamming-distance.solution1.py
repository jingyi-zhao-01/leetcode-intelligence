# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-hamming-distance
# source_path: LeetCode-Solutions-master/Python/total-hamming-distance.py
# solution_class: Solution
# submission_id: 01a408e7438b590965d72520dd8cd8b2c5e2c0a8
# seed: 143035129

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(32):
            counts = [0] * 2
            for num in nums:
                counts[(num >> i) & 1] += 1
            result += counts[0] * counts[1]
        return result