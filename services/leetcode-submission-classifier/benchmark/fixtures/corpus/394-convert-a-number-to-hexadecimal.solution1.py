# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-a-number-to-hexadecimal
# source_path: LeetCode-Solutions-master/Python/convert-a-number-to-hexadecimal.py
# solution_class: Solution
# submission_id: a5e4312de9162c3894aa3e8289af8b26530a5c94
# seed: 624797644

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"

        result = []
        while num and len(result) != 8:
            h = num & 15
            if h < 10:
                result.append(str(chr(ord('0') + h)))
            else:
                result.append(str(chr(ord('a') + h-10)))
            num >>= 4
        result.reverse()

        return "".join(result)