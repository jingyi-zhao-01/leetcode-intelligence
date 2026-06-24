# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-string
# source_path: LeetCode-Solutions-master/Python/reverse-string.py
# solution_class: Solution
# submission_id: 302c7acb00c6303018d8f16e8fa109e8b00ea8ac
# seed: 1412108793

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1