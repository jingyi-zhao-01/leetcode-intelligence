# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-type-word-using-special-typewriter
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-type-word-using-special-typewriter.py
# solution_class: Solution
# submission_id: ed8fd25af0147ea78bd5316dedd350dd8f508a8d
# seed: 3912509524

# Time:  O(n)
# Space; O(1)

class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        return (min((ord(word[0])-ord('a'))%26, (ord('a')-ord(word[0]))%26)+1) + \
               sum(min((ord(word[i])-ord(word[i-1]))%26, (ord(word[i-1])-ord(word[i]))%26)+1
                   for i in xrange(1, len(word)))