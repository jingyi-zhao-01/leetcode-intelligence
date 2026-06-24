# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-word-can-be-placed-in-crossword
# source_path: LeetCode-Solutions-master/Python/check-if-word-can-be-placed-in-crossword.py
# solution_class: Solution2
# submission_id: 3579432c89af9f1be8ff7d84b1aef41c3a3c8dac
# seed: 1745292667

# Time:  O(m * n)
# Space: O(1)

class Solution2(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        words = [word, word[::-1]]
        for mat in (board, zip(*board)):
            for row in mat:
                blocks = ''.join(row).split('#')
                for s in blocks:
                    if len(s) != len(word):
                        continue
                    for w in words:
                        if all(s[i] in (w[i], ' ') for i in xrange(len(s))):
                            return True
        return False