# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-reachable-tower
# source_path: LeetCode-Solutions-master/Python/best-reachable-tower.py
# solution_class: Solution
# submission_id: a899f2f7e279315923a2428855708dddd48a2408
# seed: 2220118291

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        best = best_x = best_y = -1
        for x, y, q in towers:
            if not abs(x-center[0])+abs(y-center[1]) <= radius:
                continue
            if q > best:
                best, best_x, best_y = q, x, y
            elif q == best and (x < best_x or (x == best_x and y < best_y)):
                best_x, best_y = x, y
        return [best_x, best_y] if best != -1 else [-1, -1]