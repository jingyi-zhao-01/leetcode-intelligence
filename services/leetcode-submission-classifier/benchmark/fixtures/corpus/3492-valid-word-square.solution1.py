# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-word-square
# source_path: LeetCode-Solutions-master/Python/valid-word-square.py
# solution_class: Solution
# submission_id: 07ef006eaec24ade973029feb5fb758e8a2d507a
# seed: 4242900164

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or \
                   words[j][i] != words[i][j]:
                   return False
        return True