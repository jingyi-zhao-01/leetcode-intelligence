# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: clear-digits
# source_path: LeetCode-Solutions-master/Python/clear-digits.py
# solution_class: Solution
# submission_id: 2f786432bb263d1e805f9d4a3b92746a5ce39a15
# seed: 3333920361

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        j = 0
        for i, x in enumerate(s):
            if x.isdigit():
                j -= 1
                continue
            s[j] = x
            j += 1
        while len(s) > j:
            s.pop()
        return "".join(s)