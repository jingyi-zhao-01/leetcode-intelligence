# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: gas-station
# source_path: LeetCode-Solutions-master/Python/gas-station.py
# solution_class: Solution
# submission_id: 796e88ce5fb720a9933acc2aed39ccbd65bc5d16
# seed: 986309892

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        start, total_sum, current_sum = 0, 0, 0
        for i in xrange(len(gas)):
            diff = gas[i] - cost[i]
            current_sum += diff
            total_sum += diff
            if current_sum < 0:
                start = i + 1
                current_sum = 0
        if total_sum >= 0:
            return start

        return -1