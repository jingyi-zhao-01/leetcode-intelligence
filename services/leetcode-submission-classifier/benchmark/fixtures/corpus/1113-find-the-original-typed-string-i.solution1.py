# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-original-typed-string-i
# source_path: LeetCode-Solutions-master/Python/find-the-original-typed-string-i.py
# solution_class: Solution
# submission_id: 117a98001a0ea1a18be1624cde982f6c849ade3a
# seed: 2992872535

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        return len(word)-sum(word[i] != word[i+1] for i in xrange(len(word)-1))