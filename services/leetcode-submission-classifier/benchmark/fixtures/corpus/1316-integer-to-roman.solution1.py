# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: integer-to-roman
# source_path: LeetCode-Solutions-master/Python/integer-to-roman.py
# solution_class: Solution
# submission_id: 5b759ff23fae338d49467ef917b97e213c6ad3b6
# seed: 4122903825

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", \
                       10: "X", 40: "XL", 50: "L", 90: "XC", \
                       100: "C", 400: "CD", 500: "D", 900: "CM", \
                       1000: "M"}
        keyset, result = sorted(numeral_map.keys()), []

        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += numeral_map[key]

        return "".join(result)