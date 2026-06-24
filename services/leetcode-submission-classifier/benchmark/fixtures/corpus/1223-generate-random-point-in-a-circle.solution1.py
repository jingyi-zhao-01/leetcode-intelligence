# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-random-point-in-a-circle
# source_path: LeetCode-Solutions-master/Python/generate-random-point-in-a-circle.py
# solution_class: Solution
# submission_id: c4fe2c6404485292d31b355e5d0ac44dc2406168
# seed: 1343226416

# Time:  O(1)
# Space: O(1)

import random
import math

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.__radius = radius
        self.__x_center = x_center
        self.__y_center = y_center
        

    def randPoint(self):
        """
        :rtype: List[float]
        """
        r = (self.__radius) * math.sqrt(random.uniform(0, 1))
        theta = (2*math.pi) * random.uniform(0, 1)
        return (r*math.cos(theta) + self.__x_center,
                r*math.sin(theta) + self.__y_center)