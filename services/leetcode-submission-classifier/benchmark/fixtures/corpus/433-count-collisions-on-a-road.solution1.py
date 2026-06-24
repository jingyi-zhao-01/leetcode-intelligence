# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-collisions-on-a-road
# source_path: LeetCode-Solutions-master/Python/count-collisions-on-a-road.py
# solution_class: Solution
# submission_id: f0e8d0fc8638e8f9a52335c0b0553c834a94c5df
# seed: 4291246669

# Time:  O(n)
# Space: O(1)

# counting, simulation

class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        result = cnt = 0
        smooth = 1
        for x in directions:
            if x == 'R':
                cnt += 1
            elif x == 'S' or (cnt or not smooth):
                result += cnt+int(x == 'L')
                cnt = smooth = 0
        return result