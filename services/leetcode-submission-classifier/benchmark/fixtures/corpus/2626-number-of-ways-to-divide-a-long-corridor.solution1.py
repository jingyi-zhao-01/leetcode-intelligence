# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-divide-a-long-corridor
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-divide-a-long-corridor.py
# solution_class: Solution
# submission_id: 6c34feeedaa200fa68aa00fd40e695c7bdd7d005
# seed: 30338517

# Time:  O(n)
# Space: O(1)

# greedy, combinatorics

class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10**9+7
        result, cnt, j = 1, 0, -1
        for i, x in enumerate(corridor):
            if x != 'S':
                continue
            cnt += 1
            if cnt >= 3 and cnt%2:
                result = result*(i-j)%MOD
            j = i
        return result if cnt and cnt%2 == 0 else 0