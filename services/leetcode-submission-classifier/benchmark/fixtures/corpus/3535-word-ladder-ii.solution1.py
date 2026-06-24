# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-ladder-ii
# source_path: LeetCode-Solutions-master/Python/word-ladder-ii.py
# solution_class: Solution
# submission_id: 1ea01f23cf7afdb3b84dad0f078f5c91744b723d
# seed: 1931200158

# Time:  O(b^(d/2)), b is the branch factor of bfs, d is the result depth
# Space: O(w * l), w is the number of words, l is the max length of words

from collections import defaultdict
from string import ascii_lowercase

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def backtracking(tree, beginWord, word): 
            return [[beginWord]] if word == beginWord else [path + [word] for new_word in tree[word] for path in backtracking(tree, beginWord, new_word)]

        words = set(wordList)
        if endWord not in words:
            return []
        tree = defaultdict(set)
        is_found, left, right, is_reversed = False, {beginWord}, {endWord}, False
        while left:
            words -= left
            new_left = set()
            for word in left:
                for new_word in (word[:i]+c+word[i+1:] for i in xrange(len(beginWord)) for c in ascii_lowercase):
                    if new_word not in words:
                        continue
                    if new_word in right: 
                        is_found = True
                    else: 
                        new_left.add(new_word)
                    tree[new_word].add(word) if not is_reversed else tree[word].add(new_word)
            if is_found:
                break
            left = new_left
            if len(left) > len(right): 
                left, right, is_reversed = right, left, not is_reversed
        return backtracking(tree, beginWord, endWord)