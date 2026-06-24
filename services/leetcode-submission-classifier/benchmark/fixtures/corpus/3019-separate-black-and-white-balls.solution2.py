# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: separate-black-and-white-balls
# source_path: LeetCode-Solutions-master/Python/separate-black-and-white-balls.py
# solution_class: Solution2
# submission_id: 07b7bc07e32c724d158d1bc4ef19bba95fcc088a
# seed: 256285646

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution2(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        left, right = 0, len(s)-1
        while left < right:
            if left < len(s) and s[left] != '1':
                left += 1
                continue
            if right >= 0 and s[right] != '0':
                right -= 1
                continue
            result += right-left
            left += 1
            right -= 1
        return result