# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-moves-to-seat-everyone
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-moves-to-seat-everyone.py
# solution_class: Solution
# submission_id: 212bd45e09be77b997aa472bd21f8a047eb3a89f
# seed: 3731345404

# Time:  O(nlogn)
# Space: O(1)

import itertools

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        return sum(abs(a-b) for a, b in itertools.izip(seats, students))