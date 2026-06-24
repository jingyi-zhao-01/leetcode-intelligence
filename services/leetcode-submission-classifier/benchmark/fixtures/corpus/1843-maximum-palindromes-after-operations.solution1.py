# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-palindromes-after-operations
# source_path: LeetCode-Solutions-master/Python/maximum-palindromes-after-operations.py
# solution_class: Solution
# submission_id: fc7a06fe7958e59d851c6aea630e1904b5a4669b
# seed: 3135446584

# Time:  O(n * l + nlogn)
# Space: O(n)

# freq table, greedy, sort

class Solution(object):
    def maxPalindromesAfterOperations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cnt = [0]*26
        for w in words:
            for c in w:
                cnt[ord(c)-ord('a')] += 1
        curr = sum(x//2 for x in cnt)
        for i, l in enumerate(sorted(map(len, words))):
            curr -= l//2
            if curr < 0:
                return i
        return len(words)