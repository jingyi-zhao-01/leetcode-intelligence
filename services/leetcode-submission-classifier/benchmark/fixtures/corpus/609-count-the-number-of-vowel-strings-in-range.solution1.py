# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-vowel-strings-in-range
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-vowel-strings-in-range.py
# solution_class: Solution
# submission_id: 4fd3d9b583467e104c4aa29a0e67912d86545cdf
# seed: 1935287964

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        return sum(words[i][0] in VOWELS and words[i][-1] in VOWELS for i in xrange(left, right+1))