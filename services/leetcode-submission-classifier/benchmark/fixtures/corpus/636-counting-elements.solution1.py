# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: counting-elements
# source_path: LeetCode-Solutions-master/Python/counting-elements.py
# solution_class: Solution
# submission_id: 20123d89f5d209b202735eab5886131afc9ddf1f
# seed: 4124763701

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lookup = set(arr)
        return sum(1 for x in arr if x+1 in lookup)