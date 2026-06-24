# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: type-of-triangle-ii
# source_path: LeetCode-Solutions-master/Python/type-of-triangle-ii.py
# solution_class: Solution
# submission_id: 014ceb964c76abaefcccac15e0617aa2880ea4b7
# seed: 2484663151

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        a, b, c = nums
        if a+b <= c:
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"