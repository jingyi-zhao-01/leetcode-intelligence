# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-initial-energy-to-finish-tasks
# source_path: LeetCode-Solutions-master/Python/minimum-initial-energy-to-finish-tasks.py
# solution_class: Solution2
# submission_id: ab09c90e99afec19fde005bfbdf2799166fc24ed
# seed: 615121234

# Time:  O(nlogn)
# Space: O(1)

class Solution2(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[0]-x[1])  # sort by save in desc
        result = curr = 0
        for a, m in tasks:  # we need to pick all the saves, so greedily to pick the most save first is always better
            result += max(m-curr, 0)
            curr = max(curr, m)-a
        return result