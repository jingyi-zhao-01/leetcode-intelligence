# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-word-distance-iii
# source_path: LeetCode-Solutions-master/Python/shortest-word-distance-iii.py
# solution_class: Solution
# submission_id: fc8ced89c987714032f79b13f146ddcecf1917fd
# seed: 1458297253

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        dist = float("inf")
        is_same = (word1 == word2)
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                if is_same and index1 is not None:
                    dist = min(dist, abs(index1 - i))
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1

        return dist