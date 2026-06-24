# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-lattice-points-inside-a-circle
# source_path: LeetCode-Solutions-master/Python/count-lattice-points-inside-a-circle.py
# solution_class: Solution
# submission_id: 6e7a46ea0ed13d9ec43fbf76508ce90929ae21e5
# seed: 1741337270

# Time:  O(n * r^2)
# Space: O(min(n * r^2, max_x * max_y))

# math, hash table

class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        lookup = set()
        for x, y, r in circles:
            for i in xrange(-r, r+1):
                for j in xrange(-r, r+1):
                    if i**2+j**2 <= r**2:
                        lookup.add(((x+i), (y+j)))
        return len(lookup)