# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lowest-common-ancestor-of-a-binary-tree-iii
# source_path: LeetCode-Solutions-master/Python/lowest-common-ancestor-of-a-binary-tree-iii.py
# solution_class: Solution
# submission_id: 4327a5aa453628ab32157c87451fe181b76bb7c3
# seed: 2437542183

# Time:  O(h)
# Space: O(1)

# Definition for a Node.
class Node:
    def __init__(self, val):
        pass

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        a, b = p, q
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a