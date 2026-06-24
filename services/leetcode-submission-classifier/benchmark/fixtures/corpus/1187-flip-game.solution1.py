# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-game
# source_path: LeetCode-Solutions-master/Python/flip-game.py
# solution_class: Solution
# submission_id: 84f40b4f0100e1c999db11709c8185b6328e0f0b
# seed: 3134175404

# Time:  O(c * n + n) = O(n * (c+1))
# Space: O(n)

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i, n = 0, len(s) - 1
        while i < n:                                    # O(n) time
            if s[i] == '+':
                while i < n and s[i+1] == '+':          # O(c) time
                    res.append(s[:i] + '--' + s[i+2:])  # O(n) time and space
                    i += 1
            i += 1
        return res