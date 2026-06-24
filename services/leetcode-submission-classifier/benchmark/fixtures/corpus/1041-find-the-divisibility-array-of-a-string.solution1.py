# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-divisibility-array-of-a-string
# source_path: LeetCode-Solutions-master/Python/find-the-divisibility-array-of-a-string.py
# solution_class: Solution
# submission_id: 3704d1f17f07f11de6aaa1a217eb0084a8ac56b1
# seed: 1526385665

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        result = []
        curr = 0
        for c in word:
            curr = (curr*10+(ord(c)-ord('0')))%m
            result.append(int(curr == 0))
        return result