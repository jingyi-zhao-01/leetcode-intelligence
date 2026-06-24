# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: keyboard-row
# source_path: LeetCode-Solutions-master/Python/keyboard-row.py
# solution_class: Solution2
# submission_id: 59e8ef78644a4f291dda64f9191db6dcad319011
# seed: 2389465998

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        single_row_words = []
        for word in words:
            for row in keyboard_rows:
                if all(letter in row for letter in word.lower()):
                    single_row_words.append(word)
        return single_row_words