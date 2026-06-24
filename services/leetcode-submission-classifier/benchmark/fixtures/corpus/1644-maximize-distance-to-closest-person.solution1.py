# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-distance-to-closest-person
# source_path: LeetCode-Solutions-master/Python/maximize-distance-to-closest-person.py
# solution_class: Solution
# submission_id: ea47b84a566e53842a0f306ad91b499b13a6d38d
# seed: 190496052

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev, result = -1, 1
        for i in xrange(len(seats)):
            if seats[i]:
                if prev < 0:
                    result = i
                else:
                    result = max(result, (i-prev)//2)
                prev = i
        return max(result, len(seats)-1-prev)