# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-ladder
# source_path: LeetCode-Solutions-master/Python/word-ladder.py
# solution_class: Solution
# submission_id: 992eb7317a732c1713b4916c25e64dfae5149c08
# seed: 793692051

# Time:  O(b^(d/2)), b is the branch factor of bfs, d is the result depth
# Space: O(w * l), w is the number of words, l is the max length of words

from string import ascii_lowercase


# two-end bfs

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set(wordList)
        if endWord not in words:
            return 0
        left, right = {beginWord}, {endWord}
        ladder = 2
        while left:
            words -= left
            new_left = set()
            for word in left:
                for new_word in (word[:i]+c+word[i+1:] for i in xrange(len(beginWord)) for c in ascii_lowercase):
                    if new_word not in words:
                        continue
                    if new_word in right: 
                        return ladder
                    new_left.add(new_word)
            left = new_left
            ladder += 1
            if len(left) > len(right): 
                left, right = right, left
        return 0