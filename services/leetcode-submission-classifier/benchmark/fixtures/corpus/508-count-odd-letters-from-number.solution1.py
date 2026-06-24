# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-odd-letters-from-number
# source_path: LeetCode-Solutions-master/Python/count-odd-letters-from-number.py
# solution_class: Solution
# submission_id: a99a3166a523c0aa7c0b46ee21f3c9275d112ab9
# seed: 3276699503

# Time:  O(logn)
# Space: O(26)

# freq table

class Solution(object):
    def countOddLetters(self, n):
        """
        :type n: int
        :rtype: int
        """
        lookup = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        cnt = [0]*26
        while n:
            n, d = divmod(n, 10)
            for x in lookup[d]:
                cnt[ord(x)-ord('a')] += 1
        return sum(v%2 for v in cnt)