# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-max-distance-to-gas-station
# source_path: LeetCode-Solutions-master/Python/minimize-max-distance-to-gas-station.py
# solution_class: Solution
# submission_id: a630807e712a180332e09f92b6d2766a649fc41f
# seed: 2654647766

# Time:  O(nlogr)
# Space: O(1)

import math

class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        def check(x):
            return sum(int(math.ceil((stations[i+1]-stations[i])/x))-1 for i in xrange(len(stations)-1)) <= K

        left, right = 0, stations[-1]-stations[0]
        while right-left > 1e-6:
            mid = left + (right-left)/2.0
            if check(mid):
                right = mid
            else:
                left = mid
        return left