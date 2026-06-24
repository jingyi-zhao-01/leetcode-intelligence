# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sorting-the-sentence
# source_path: LeetCode-Solutions-master/Python/sorting-the-sentence.py
# solution_class: Solution
# submission_id: 88ebd10ef21e12dd3be36f6ba348dcc4e8050175
# seed: 3980565278

# Time:  O(n)
# Space: O(n)

import itertools

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i in xrange(len(words)):
            while int(words[i][-1])-1 != i:
                words[int(words[i][-1])-1], words[i] = words[i], words[int(words[i][-1])-1]
        return " ".join(itertools.imap(lambda x: x[:-1], words))