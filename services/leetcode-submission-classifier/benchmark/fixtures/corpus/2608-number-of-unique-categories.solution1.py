# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-unique-categories
# source_path: LeetCode-Solutions-master/Python/number-of-unique-categories.py
# solution_class: Solution
# submission_id: c4031f720237630573d553735cdbd273ef29474c
# seed: 4237704978

# Time:  O(n^2)
# Space: O(1)

# Definition for a category handler.
class CategoryHandler:
    def haveSameCategory(self, a, b):
        pass


# brute force

class Solution(object):
    def numberOfCategories(self, n, categoryHandler):
        """
        :type n: int
        :type categoryHandler: CategoryHandler
        :rtype: int
        """
        return sum(all(not categoryHandler.haveSameCategory(j, i) for j in xrange(i)) for i in xrange(n))