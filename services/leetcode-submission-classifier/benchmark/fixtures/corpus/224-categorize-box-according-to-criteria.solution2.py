# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: categorize-box-according-to-criteria
# source_path: LeetCode-Solutions-master/Python/categorize-box-according-to-criteria.py
# solution_class: Solution2
# submission_id: 00404b6f97a7ab81a9a42cabb1e17c273cf8b80a
# seed: 2187993451

# Time:  O(1)
# Space: O(1)

# math, implementation

class Solution2(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        CATEGORIES = ["Neither", "Heavy", "Bulky", "Both"]
        i = 2*(any(x >= 10**4 for x in (length, width, height)) or length*width*height >= 10**9)+int(mass >= 100)
        return CATEGORIES[i]