# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rectangle-area
# source_path: LeetCode-Solutions-master/Python/rectangle-area.py
# solution_class: Solution
# submission_id: 8366416cc2f4a60d389e80f2c9186a8b07221347
# seed: 3653420251

# Time:  O(1)
# Space: O(1)

class Solution(object):
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (D - B) * (C - A) + \
               (G - E) * (H - F) - \
               max(0, (min(C, G) - max(A, E))) * \
               max(0, (min(D, H) - max(B, F)))