# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: can-place-flowers
# source_path: LeetCode-Solutions-master/Python/can-place-flowers.py
# solution_class: Solution
# submission_id: 5da0220fbb47c66684d871609bdb821194cb5e34
# seed: 3498271373

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in xrange(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and \
                (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False