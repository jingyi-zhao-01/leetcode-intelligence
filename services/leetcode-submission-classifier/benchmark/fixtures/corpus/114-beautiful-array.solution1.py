# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: beautiful-array
# source_path: LeetCode-Solutions-master/Python/beautiful-array.py
# solution_class: Solution
# submission_id: 300d4596a51beb1676caff8602a76843c43db8ca
# seed: 3718597280

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        result = [1]
        while len(result) < N:
            result = [i*2 - 1 for i in result] + [i*2 for i in result]
        return [i for i in result if i <= N]