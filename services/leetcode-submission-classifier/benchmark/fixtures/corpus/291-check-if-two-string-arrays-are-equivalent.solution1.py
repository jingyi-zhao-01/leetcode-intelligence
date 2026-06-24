# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-two-string-arrays-are-equivalent
# source_path: LeetCode-Solutions-master/Python/check-if-two-string-arrays-are-equivalent.py
# solution_class: Solution
# submission_id: 27835dddb82144b9d3495af01806c26293521c29
# seed: 3856424675

# Time:  O(n), n is the total length of word1 and word2
# Space: O(1)

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        idx1 = idx2 = arr_idx1 = arr_idx2 = 0
        while arr_idx1 < len(word1) and arr_idx2 < len(word2):
            if word1[arr_idx1][idx1] != word2[arr_idx2][idx2]:
                break
            idx1 += 1
            if idx1 == len(word1[arr_idx1]):
                idx1 = 0
                arr_idx1 += 1
            idx2 += 1
            if idx2 == len(word2[arr_idx2]):
                idx2 = 0
                arr_idx2 += 1
        return arr_idx1 == len(word1) and arr_idx2 == len(word2)