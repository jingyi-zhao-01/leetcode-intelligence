# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: corporate-flight-bookings
# source_path: LeetCode-Solutions-master/Python/corporate-flight-bookings.py
# solution_class: Solution
# submission_id: bc17b1a37e4ad9d6488203bde6a970d23a93ae6a
# seed: 2086985182

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        result = [0]*(n+1)
        for i, j, k in bookings:
            result[i-1] += k
            result[j] -= k
        for i in xrange(1, len(result)):
            result[i] += result[i-1]
        result.pop()
        return result