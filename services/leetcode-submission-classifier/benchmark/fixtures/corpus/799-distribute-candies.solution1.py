# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-candies
# source_path: LeetCode-Solutions-master/Python/distribute-candies.py
# solution_class: Solution
# submission_id: dcc07ef9617a065e9785fa951fd033322a2b73ee
# seed: 3390623368

# Time:  O(n)
# Space: O(n)

class Solution(object):

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        lookup = set(candies)
        return min(len(lookup), len(candies)/2)