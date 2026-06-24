# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-distance-traveled
# source_path: LeetCode-Solutions-master/Python/total-distance-traveled.py
# solution_class: Solution
# submission_id: 431ef9ad0d0afc16c2a4d68d69abfffb34fe4798
# seed: 1730883037

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        USE, REFILL, DIST = 5, 1, 10
        cnt = min((mainTank-REFILL)//(USE-REFILL), additionalTank)
        return (mainTank+cnt*REFILL)*DIST