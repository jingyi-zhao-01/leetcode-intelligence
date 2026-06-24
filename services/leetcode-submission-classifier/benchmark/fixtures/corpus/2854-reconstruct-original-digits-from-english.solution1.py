# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reconstruct-original-digits-from-english
# source_path: LeetCode-Solutions-master/Python/reconstruct-original-digits-from-english.py
# solution_class: Solution
# submission_id: abbfd2ab8cfa8e4d8adb377fb175d410960597a6
# seed: 1967069151

# Time:  O(n)
# Space: O(1)

from collections import Counter

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The count of each char in each number string.
        cnts = [Counter(_) for _ in ["zero", "one", "two", "three", \
                                     "four", "five", "six", "seven", \
                                     "eight", "nine"]]

        # The order for greedy method.
        order = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

        # The unique char in the order.
        unique_chars = ['z', 'o', 'w', 't', 'u', \
                        'f', 'x', 's', 'g', 'n']

        cnt = Counter(list(s))
        res = []
        for i in order:
            while cnt[unique_chars[i]] > 0:
                cnt -= cnts[i]
                res.append(i)
        res.sort()

        return "".join(map(str, res))