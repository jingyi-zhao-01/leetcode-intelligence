# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: car-pooling
# source_path: LeetCode-Solutions-master/Python/car-pooling.py
# solution_class: Solution
# submission_id: 8fead4205fb73cb3989142e84e675103269c27dd
# seed: 1089767921

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        line = [x for num, start, end in trips for x in [[start, num], [end, -num]]]
        line.sort()
        for _, num in line:
            capacity -= num
            if capacity < 0:
                return False
        return True