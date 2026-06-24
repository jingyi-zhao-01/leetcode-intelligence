# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kids-with-the-greatest-number-of-candies
# source_path: LeetCode-Solutions-master/Python/kids-with-the-greatest-number-of-candies.py
# solution_class: Solution
# submission_id: e72893880a9782538cf11cefda782317d7de80b3
# seed: 3551082962

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = max(candies)
        return [x + extraCandies >= max_num for x in candies]