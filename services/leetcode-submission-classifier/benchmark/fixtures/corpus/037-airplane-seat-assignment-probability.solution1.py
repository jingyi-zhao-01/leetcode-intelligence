# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: airplane-seat-assignment-probability
# source_path: LeetCode-Solutions-master/Python/airplane-seat-assignment-probability.py
# solution_class: Solution
# submission_id: 8d89eba0bb98e94700810c72dc67f2c52b64fc1f
# seed: 99243331

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        # p(k) = 1 * (prob that 1th passenger takes his own seat) +
        #        0 * (prob that 1th passenger takes kth one's seat) +
        #        1 * (prob that 1th passenger takes the others' seat) * 
        #            (prob that the first k-1 passengers get a seat
        #             which is not kth one's seat)
        #      = 1/k + p(k-1)*(k-2)/k
        #
        # p(1) = 1
        # p(2) = 1/2 + p(1) * (2-2)/2 = 1/2
        # p(3) = 1/3 + p(2) * (3-2)/3 = 1/3 + 1/2 * (3-2)/3 = 1/2
        # ...
        # p(n) = 1/n + 1/2 * (n-2)/n = (2+n-2)/(2n) = 1/2
        return 0.5 if n != 1 else 1.0