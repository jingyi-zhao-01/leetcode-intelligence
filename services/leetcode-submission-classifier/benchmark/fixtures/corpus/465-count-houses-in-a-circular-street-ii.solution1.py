# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-houses-in-a-circular-street-ii
# source_path: LeetCode-Solutions-master/Python/count-houses-in-a-circular-street-ii.py
# solution_class: Solution
# submission_id: 4453b874dcd3416071d38ffe10aba3969e67b744
# seed: 2106943501

# Time:  O(k)
# Space: O(1)

# Definition for a street.
class Street:
    def closeDoor(self):
        pass
    def isDoorOpen(self):
        pass
    def moveRight(self):
        pass


# constructive algorithms

class Solution(object):
    def houseCount(self, street, k):
        """
        :type street: Street
        :type k: int
        :rtype: int
        """
        while not street.isDoorOpen():
            street.moveRight()
        result = 0
        for i in xrange(k+1):
            if i and street.isDoorOpen():
                street.closeDoor()
                result = i
            street.moveRight()
        return result