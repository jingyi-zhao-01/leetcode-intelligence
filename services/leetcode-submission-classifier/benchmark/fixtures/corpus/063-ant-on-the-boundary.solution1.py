# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ant-on-the-boundary
# source_path: LeetCode-Solutions-master/Python/ant-on-the-boundary.py
# solution_class: Solution
# submission_id: c92f3320f52f40c231b590a5ce529f94f77aa4ff
# seed: 1829705217

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = curr = 0
        for x in nums:
            curr += x
            if curr == 0:
                result += 1
        return result