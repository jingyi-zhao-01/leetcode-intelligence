# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-k-th-character-in-string-game-i
# source_path: LeetCode-Solutions-master/Python/find-the-k-th-character-in-string-game-i.py
# solution_class: Solution
# submission_id: 56167020b3faf55ead1b91bbc146195aa0b9a11f
# seed: 2949590445

# Time:  O(1)
# Space: O(1)

# bitmasks

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        def popcount(x):
            return bin(x)[2:].count('1')

        return chr(ord('a')+popcount(k-1)%26)