# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-strings-alternately
# source_path: LeetCode-Solutions-master/Python/merge-strings-alternately.py
# solution_class: Solution
# submission_id: 61d8bd0f11b956dcc8179decd66dc2634725c314
# seed: 3814127109

# Time:  O(m + n)
# Space: O(1)

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return "".join(result)