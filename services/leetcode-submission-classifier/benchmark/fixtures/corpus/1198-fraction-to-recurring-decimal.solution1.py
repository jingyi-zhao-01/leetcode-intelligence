# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fraction-to-recurring-decimal
# source_path: LeetCode-Solutions-master/Python/fraction-to-recurring-decimal.py
# solution_class: Solution
# submission_id: 6ae9ffd13aa9b53894e6e28e98549d2ab72d0609
# seed: 626256859

# Time:  O(logn), where logn is the length of result strings
# Space: O(1)

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            result = "-"

        dvd, dvs = abs(numerator), abs(denominator)
        result += str(dvd / dvs)
        dvd %= dvs

        if dvd > 0:
            result += "."

        lookup = {}
        while dvd and dvd not in lookup:
            lookup[dvd] = len(result)
            dvd *= 10
            result += str(dvd / dvs)
            dvd %= dvs

        if dvd in lookup:
            result = result[:lookup[dvd]] + "(" + result[lookup[dvd]:] + ")"

        return result