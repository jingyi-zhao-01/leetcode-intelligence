# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: hexspeak
# source_path: LeetCode-Solutions-master/Python/hexspeak.py
# solution_class: Solution2
# submission_id: 7519a94041dec03ddd3485330ad6f2d4f9549e20
# seed: 535631313

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = hex(int(num)).upper()[2:].replace('0', 'O').replace('1', 'I')
        return result if all(c in "ABCDEFOI" for c in result) else "ERROR"