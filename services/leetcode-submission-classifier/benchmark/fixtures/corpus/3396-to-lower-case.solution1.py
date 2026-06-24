# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: to-lower-case
# source_path: LeetCode-Solutions-master/Python/to-lower-case.py
# solution_class: Solution
# submission_id: 17e826e088191c23245d62c2819b7be2b5c284d2
# seed: 2977983095

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([chr(ord('a')+ord(c)-ord('A')) 
                        if 'A' <= c <= 'Z' else c for c in str])