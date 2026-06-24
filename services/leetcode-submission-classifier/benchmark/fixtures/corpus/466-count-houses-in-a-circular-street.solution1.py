# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-houses-in-a-circular-street
# source_path: LeetCode-Solutions-master/Python/count-houses-in-a-circular-street.py
# solution_class: Solution
# submission_id: 132c524583486ae3aee4bb57dd3aef393f221033
# seed: 3299957357

# Time:  O(k)
# Space: O(1)

# Definition for a street.
class Street:
    def openDoor(self):
        pass
    def closeDoor(self):
        pass
    def isDoorOpen(self):
        pass
    def moveRight(self):
        pass
    def moveLeft(self):
        pass


# constructive algorithms

class Solution(object):
    def houseCount(self, street, k):
        """
        :type street: Street
        :type k: int
        :rtype: int
        """
        for _ in xrange(k):
            street.closeDoor()
            street.moveRight()
        for result in xrange(k+1):
            if street.isDoorOpen():
                break
            street.openDoor()
            street.moveRight()
        return result