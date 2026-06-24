# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: guess-the-word
# source_path: LeetCode-Solutions-master/Python/guess-the-word.py
# solution_class: Solution2
# submission_id: c49517d8752ef65fa8a33371087a4850bcb1caef
# seed: 749984846

# Time:  O(n)
# Space: O(n)

import collections
import itertools

class Solution2(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def solve(H, possible):
            min_max_group, best_guess = possible, None
            for guess in possible:
                groups = [[] for _ in xrange(7)]
                for j in possible:
                    if j != guess:
                        groups[H[guess][j]].append(j)
                max_group = max(groups, key=len)
                if len(max_group) < len(min_max_group):
                    min_max_group, best_guess = max_group, guess
            return best_guess

        H = [[sum(a == b for a, b in itertools.izip(wordlist[i], wordlist[j]))
                  for j in xrange(len(wordlist))]
                  for i in xrange(len(wordlist))]
        possible = range(len(wordlist))
        n = 0
        while n < 6:
            guess = solve(H, possible)
            n = master.guess(wordlist[guess])
            possible = [j for j in possible if H[guess][j] == n]