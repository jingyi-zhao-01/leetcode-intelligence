# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-original-typed-string-i
# source_path: LeetCode-Solutions-master/Python/find-the-original-typed-string-i.py
# solution_class: Solution2
# submission_id: 3e2d1a248500fe915f5b0b835484e2f535c228ea
# seed: 3316168882

# Time:  O(n)
# Space: O(1)

# array

class Solution2(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = 1
        curr = 0
        for i in xrange(len(word)):
            curr += 1
            if i+1 == len(word) or word[i+1] != word[i]:
                result += curr-1
                curr = 0
        return result