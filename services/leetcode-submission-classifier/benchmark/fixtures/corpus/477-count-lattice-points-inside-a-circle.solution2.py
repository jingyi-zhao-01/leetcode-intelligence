# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-lattice-points-inside-a-circle
# source_path: LeetCode-Solutions-master/Python/count-lattice-points-inside-a-circle.py
# solution_class: Solution2
# submission_id: e299c631394c7cea801a9fd1a5a66e5493187a7b
# seed: 2949146608

# Time:  O(n * r^2)
# Space: O(min(n * r^2, max_x * max_y))

# math, hash table

class Solution2(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        max_x = max(x+r for x, _, r in circles)
        max_y = max(y+r for _, y, r in circles)
        result = 0
        for i in xrange(max_x+1):
            for j in xrange(max_y+1):
                if any((i-x)**2+(j-y)**2 <= r**2 for x, y, r in circles):
                    result += 1
        return result