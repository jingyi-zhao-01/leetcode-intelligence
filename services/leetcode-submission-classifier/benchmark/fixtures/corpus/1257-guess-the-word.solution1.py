# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: guess-the-word
# source_path: LeetCode-Solutions-master/Python/guess-the-word.py
# solution_class: Solution
# submission_id: 8c667a3b3ca691a94819ba33abc60187ea2c29f7
# seed: 2573039538

# Time:  O(n)
# Space: O(n)

import collections
import itertools

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        possible = range(len(wordlist))
        n = 0
        while n < 6:
            count = [collections.Counter(w[i] for w in wordlist) for i in xrange(6)]
            guess = max(possible, key=lambda x: sum(count[i][c] for i, c in enumerate(wordlist[x])))
            n = master.guess(wordlist[guess])
            possible = [j for j in possible if sum(a == b for a, b in itertools.izip(wordlist[guess], wordlist[j])) == n]