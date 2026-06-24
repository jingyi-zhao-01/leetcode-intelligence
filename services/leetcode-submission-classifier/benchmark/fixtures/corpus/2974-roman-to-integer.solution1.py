# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: roman-to-integer
# source_path: LeetCode-Solutions-master/Python/roman-to-integer.py
# solution_class: Solution
# submission_id: 2377f76698c2b61ab285536ba6fe912213c91492
# seed: 2357146914

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in xrange(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal