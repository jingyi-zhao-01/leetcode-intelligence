# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: hamming-distance
# source_path: LeetCode-Solutions-master/Python/hamming-distance.py
# solution_class: Solution
# submission_id: 802582f6c02581ed5c9c291d466e228bbf659407
# seed: 779377796

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        z = x ^ y
        while z:
            distance += 1
            z &= z - 1
        return distance

    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')