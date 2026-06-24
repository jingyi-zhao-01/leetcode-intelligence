# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: second-largest-digit-in-a-string
# source_path: LeetCode-Solutions-master/Python/second-largest-digit-in-a-string.py
# solution_class: Solution
# submission_id: 4539b114e484150a6d242855605a4305c243a169
# seed: 3625944491

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = second = -1
        for c in s:
            if not c.isdigit():
                continue
            d = int(c)
            if d > first:
                first, second = d, first
            elif first > d > second:
                second = d
        return second