# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: categorize-box-according-to-criteria
# source_path: LeetCode-Solutions-master/Python/categorize-box-according-to-criteria.py
# solution_class: Solution
# submission_id: 615408df59e80c95ad06a9250f1de721e2fc00dc
# seed: 608641104

# Time:  O(1)
# Space: O(1)

# math, implementation

class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        bulky = any(x >= 10**4 for x in (length, width, height)) or length*width*height >= 10**9
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"