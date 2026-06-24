# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-reachable-tower
# source_path: LeetCode-Solutions-master/Python/best-reachable-tower.py
# solution_class: Solution2
# submission_id: 3257bb727697d6576807b44b37a5079f866a4a7b
# seed: 193573571

# Time:  O(n)
# Space: O(1)

# array

class Solution2(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        result = [1]*3
        for x, y, q in towers:
            if not abs(x-center[0])+abs(y-center[1]) <= radius:
                continue
            result = min(result, [-q, x, y])
        return result[1:] if result[0] != 1 else [-1, -1]