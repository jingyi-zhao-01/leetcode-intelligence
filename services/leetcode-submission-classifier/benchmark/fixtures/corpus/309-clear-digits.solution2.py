# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: clear-digits
# source_path: LeetCode-Solutions-master/Python/clear-digits.py
# solution_class: Solution2
# submission_id: 2c756b111dc9b9657384876ec4c3c718ad3a1ff7
# seed: 1921297309

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution2(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for x in s:
            if x.isdigit():
                result.pop()
                continue
            result.append(x)
        return "".join(result)