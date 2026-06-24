# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-tested-devices-after-test-operations
# source_path: LeetCode-Solutions-master/Python/count-tested-devices-after-test-operations.py
# solution_class: Solution
# submission_id: b598364a2bf2ec1d255b80a4fcff12fb5d151ccd
# seed: 1746607812

# Time:  O(n)
# Space: O(1)

# simulation

class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        result = 0
        for x in batteryPercentages:
            if x > result:
                result += 1
        return result