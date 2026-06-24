# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-a-string-in-balanced-strings
# source_path: LeetCode-Solutions-master/Python/split-a-string-in-balanced-strings.py
# solution_class: Solution
# submission_id: 7e38a5d1dd75118d2878497fda62839e8c655d81
# seed: 3580100100

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, count = 0, 0      
        for c in s:
            count += 1 if c == 'L' else -1            
            if count == 0:
                result += 1
        return result