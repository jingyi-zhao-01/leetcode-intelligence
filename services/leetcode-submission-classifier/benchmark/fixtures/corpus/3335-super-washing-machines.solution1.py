# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: super-washing-machines
# source_path: LeetCode-Solutions-master/Python/super-washing-machines.py
# solution_class: Solution
# submission_id: 356a2b46d42f9e9e05c433b355e59b329c114fff
# seed: 3123554818

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        if total % len(machines): return -1

        result, target, curr = 0, total / len(machines), 0
        for n in machines:
            curr += n - target
            result = max(result, max(n - target, abs(curr)))
        return result