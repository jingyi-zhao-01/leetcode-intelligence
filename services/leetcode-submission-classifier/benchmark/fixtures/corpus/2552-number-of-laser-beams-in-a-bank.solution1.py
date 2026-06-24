# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-laser-beams-in-a-bank
# source_path: LeetCode-Solutions-master/Python/number-of-laser-beams-in-a-bank.py
# solution_class: Solution
# submission_id: fb6b776040f1d89c02fd879d03b77a26f4b14951
# seed: 1611437017

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        result = prev = 0
        for x in bank:
            cnt = x.count('1')
            if not cnt:
                continue
            result += prev*cnt
            prev = cnt
        return result